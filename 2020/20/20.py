#!/usr/bin/python3
import copy
import random

with open('tiles.txt') as fh:
    lines = fh.readlines()

tilestrs = ''.join(lines).split('\n\n')
tilestrs = {int(t.split('\n')[0][5:9]):'\n'.join(t.strip().split('\n')[1:]) for t in tilestrs}

tiles = {}
for tilekey,tilestr in tilestrs.items():
    tile = []
    for rowstr in tilestr.split('\n'):
        tile.append(rowstr.strip())
    tiles[tilekey] = tile

def ptile(tile):
    print('\n'.join([' '.join(r) for r in tile]))


def vreflect(tile):
    return [t for t in list(reversed(tile))]

def hreflect(tile):
    return [list(reversed(t)) for t in tile]

def rotate(tile, degree):
    ttile = tile
    res = ttile
    while degree > 0:
        res = [['' for c in range(len(ttile))] for r in range(len(ttile[0]))]

        for row in range(len(ttile[0])):
            for col in range(len(ttile)):
                res[row-1][col] = ttile[col][-row]
        ttile = res
        degree -= 1
    return res

def transform(tile, vref, href, rot):
    ttile = tile
    if vref:
        ttile = vreflect(ttile)
    if href:
        ttile = hreflect(ttile)
    if rot:
        ttile = rotate(ttile, rot)
    return ttile

def memohash(vref, href, rot):
    return (100 if vref else 0) + (10 if href else 0) + rot

memo = {}
def memoget(id, vref, href, rot):
    if id not in memo:
        return None
    return memo[id].get(memohash(vref, href, rot), None)

def memoset(id, vref, href, rot, tile):
    if id not in memo:
        memo[id] = {}
    memo[id][memohash(vref, href, rot)] = tile

def variants(id):
    vars = []
    for vref in [False,True]:
        for href in [False,True]:
            for rot in range(0,4):
                v = memoget(id, vref, href, rot)
                if not v:
                    v = transform(tiles[id], vref, href, rot)
                    memoset(id, vref, href, rot, v)
                vars.append((id,vref,href,rot))
    return vars

def fit(tile, othertile, pos):
    # Pos = 0 -> other is to the right
    # Pos = 1 -> other is above
    # Pos = 2 -> other is to the left
    # Pos = 3 -> other is below

    if pos == 0:
        edge = [r[-1] for r in tile]
        otheredge = [r[0] for r in othertile]
    if pos == 1:
        edge = tile[0]
        otheredge = othertile[-1]
    if pos == 2:
        edge = [r[0] for r in tile]
        otheredge = [r[-1] for r in othertile]
    if pos == 3:
        edge = tile[-1]
        otheredge = othertile[0]

    for (e,o) in zip(edge,otheredge):
        if e != o:
            return False
    return True

def memofithash(memotile, othermemotile, pos):
    return str(memotile) + str(othermemotile) + str(pos)

memofitd = {}

def memofit(memotile, othermemotile, pos):
    mfh = memofithash(memotile, othermemotile, pos)
    if mfh not in memofitd:
        memofitd[mfh] = fit(memoget(*memotile),memoget(*othermemotile),pos)
    return memofitd[mfh]

# I counted 144 tiles, so it's a 12x12 square. If we use one of the corners as
# the starting point, then we need enough room for the whole puzzle to fill one
# quadrant. So use a 23x23 grid. For algorithmic simplicity, add an extra border
# slots around the edge
grid = [[None for _ in range(25)] for _ in range(25)]

pool = list(tiles.keys())
random.shuffle(list(reversed(pool)))

# Arbitrarily select tile 1669 as the starting point, with no transformations
grid[12][12] = (1669,0,0,0)
pool.remove(1669)
variants(1669)

def solve():
    for row in range(len(grid)):
        for col in range(len(grid)):
            print(('[' + str(grid[row][col][0]) + ']' if grid[row][col] else '......'), end='')
        print('')
    print(pool)

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            # If cell is already filled, we can't add a tile to it
            if grid[row][col]:
                continue
            # If no neighbours are filled, don't waste time on this cell.
            # This is the part that benefits from the extra border
            right = grid[row][col+1]
            above = grid[row-1][col]
            left = grid[row][col-1]
            below = grid[row+1][col]
            if not right and not above and not left and not below:
                continue

            # Try all variants of all tiles from the pool
            for id in pool:
                for variant in variants(id):
                    if right and not memofit(variant, right, 0):
                        continue
                    if above and not memofit(variant, above, 1):
                        continue
                    if left and not memofit(variant, left, 2):
                        continue
                    if below and not memofit(variant, below, 3):
                        continue
                    # Found a variant that works. Remove from the pool, add to the
                    # grid, and recurse
                    idx = pool.index(id)
                    pool.remove(id)
                    grid[row][col] = variant
                    solve()

                    # If the pool is empty after recursing, we have a solution.
                    if not pool:
                        return

                    # Otherwise the solve failed and we are backtracking. Try
                    # the next variant.
                    grid[row][col] = None
                    pool.insert(idx,id)
solve()

for id,variants in memo.items():
    for mh,variant in variants.items():
        pruned = copy.deepcopy(variant)
        pruned = pruned[1:-1]
        pruned = [p[1:-1] for p in pruned]
        memo[id][mh] = pruned

minrow = 0
for (idx,row) in enumerate(grid):
    filled = 0
    for cell in row:
        if cell:
            filled = 1
            break
    if filled:
        minrow = idx
        break

maxrow = 0
for (idx,row) in reversed(list(enumerate(grid))):
    filled = 0
    for cell in row:
        if cell:
            filled = 1
            break
    if filled:
        maxrow = idx
        break

mincol = 0
for (idx,cell) in enumerate(grid[minrow]):
    if cell:
        mincol = idx
        break

maxcol = 0
for (idx,cell) in reversed(list(enumerate(grid[maxrow]))):
    if cell:
        maxcol = idx
        break

trimmedgrid = grid[minrow:maxrow+1]

for idx,row in enumerate(trimmedgrid):
    trimmedgrid[idx] = row[mincol:maxcol+1]

imagetiles = [[memoget(*c) for c in r] for r in trimmedgrid]

image = []
for tilerow in imagetiles:
    for subrowidx in range(8):
        subrow = []
        for tile in tilerow:
            subrow += tile[subrowidx]
        image.append(subrow)

monsterimg = [list('                  # '),
              list('#    ##    ##    ###'),
              list(' #  #  #  #  #  #   ')]

monstervariants = []
for vref in [False,True]:
    for href in [False,True]:
        for rot in range(0,4):
            monstervariants.append(transform(monsterimg, vref, href, rot))

for mvar in monstervariants:
    for mrow in (mvar):
        print(''.join(mrow))
    print('')

inmonster = [[False for _ in r] for r in image]

def checkmonster(row, col, monster):
    if row + len(monster) > len(image):
        return False
    if col + len(monster[0]) > len(image[row]):
        return False

    for mrow in range(len(monster)):
        for mcol in range(len(monster[mrow])):
            if monster[mrow][mcol] == '#' and image[row+mrow][col+mcol] != '#':
                return False
    return True

for row in range(len(image)):
    for col in range(len(image[row])):
        for mvar in monstervariants:
            if checkmonster(row, col, mvar):
                for mrow in range(len(mvar)):
                    for mcol in range(len(mvar[mrow])):
                        if mvar[mrow][mcol] == '#':
                            inmonster[row+mrow][col+mcol] = True

print('\n'.join([' '.join(r) for r in image]))
print('\n'.join(' '.join([{True:'#',False:' '}[c] for c in r]) for r in inmonster))

monstercount = 0
nonmonstercount = 0
for row in range(len(image)):
    for col in range(len(image)):
        if image[row][col] != '#':
            continue
        if inmonster[row][col]:
            monstercount += 1
        else:
            nonmonstercount += 1

print(nonmonstercount)
