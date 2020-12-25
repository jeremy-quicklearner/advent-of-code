#!/usr/bin/python3
import copy

with open('seats.txt') as fh:
    lines = fh.readlines()

grid = [[{'.':None,'L':False}[c] for c in l.strip()] for l in lines]
for row in grid:
    row.append(None)
    row.insert(0, None)

grid.insert(0, [None for c in grid[0]])
grid.append([None for c in grid[0]])

def iterate1(g):
    ng = copy.deepcopy(g)
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col] is not None:
                c = g[row][col]
                n = 0
                if g[row-1][col-1]:
                    n += 1
                if g[row-1][col+1]:
                    n += 1
                if g[row+1][col-1]:
                    n += 1
                if g[row+1][col+1]:
                    n += 1
                if g[row][col-1]:
                    n += 1
                if g[row][col+1]:
                    n += 1
                if g[row-1][col]:
                    n += 1
                if g[row+1][col]:
                    n += 1

                if c == False and n == 0:
                    ng[row][col] = True
                elif c == True and n >= 4:
                    ng[row][col] = False
    return ng

def traverse(g, startrow, startcol, rowstep, colstep):
    row = startrow + rowstep
    col = startcol + colstep
    while True:
        if row < 0 or col < 0 or row >= len(g) or col >= len(g[row]):
            return False
        if g[row][col] is not None:
            return g[row][col]
        row = row + rowstep
        col = col + colstep

def iterate2(g):
    ng = copy.deepcopy(g)
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col] is not None:
                c = g[row][col]
                n = 0
                if traverse(g,row,col,-1,-1):
                    n += 1
                if traverse(g,row,col,-1, 1):
                    n += 1
                if traverse(g,row,col, 1,-1):
                    n += 1
                if traverse(g,row,col, 1, 1):
                    n += 1
                if traverse(g,row,col, 0,-1):
                    n += 1
                if traverse(g,row,col, 0, 1):
                    n += 1
                if traverse(g,row,col,-1, 0):
                    n += 1
                if traverse(g,row,col, 1, 0):
                    n += 1

                if c == False and n == 0:
                    ng[row][col] = True
                elif c == True and n >= 5:
                    ng[row][col] = False
    return ng

def equals(g, ng):
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col] != ng[row][col]:
                return False
    return True

def count(g):
    acc = 0
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col]:
                acc += 1
    return acc

while(True):
    newgrid = iterate2(grid)
    if equals(grid, newgrid):
        break
    grid = newgrid

print(count(grid))
