#!/usr/bin/python
import copy

with open('pat.txt') as fh:
    lines = fh.readlines()

tiles = [[0 for _ in range(250)] for __ in range(250)]

for ppath in lines:
    path = ppath
    (x,y) = (150,150)
    while(path):
        if path[0] == 'e':
            (x,y) = (x-1,y-1)
            path = path[1:]
        if path[0] == 'w':
            (x,y) = (x+1,y+1)
            path = path[1:]
        if path[0:2] == 'ne':
            (x,y) = (x,y-1)
            path = path[2:]
        if path[0:2] == 'nw':
            (x,y) = (x+1,y)
            path = path[2:]
        if path[0:2] == 'se':
            (x,y) = (x-1,y)
            path = path[2:]
        if path[0:2] == 'sw':
            (x,y) = (x,y+1)
            path = path[2:]
        if path[0] == '\n':
            path = ''

    key = '%d,%d' % (x,y)
    tiles[x][y] = 1 - tiles[x][y]

print(sum([sum(row) for row in tiles]))

for it in range(100):
    newtiles = copy.deepcopy(tiles)

    for x in range(1,len(tiles)-1):
        for y in range(1,len(tiles[x])-1):
            neigh = 0
            if tiles[x-1][y-1] == 1:
                neigh += 1
            if tiles[x+1][y+1] == 1:
                neigh += 1
            if tiles[x][y-1] == 1:
                neigh += 1
            if tiles[x+1][y] == 1:
                neigh += 1
            if tiles[x-1][y] == 1:
                neigh += 1
            if tiles[x][y+1] == 1:
                neigh += 1
            
            if tiles[x][y] == 1:
                if neigh == 0 or neigh > 2:
                    newtiles[x][y] = 0
                else:
                    newtiles[x][y] = 1
            else:
                if neigh == 2:
                    newtiles[x][y] = 1
                else:
                    newtiles[x][y] = 0
    tiles = newtiles
    print('%d:%d' % (it,sum([sum(row) for row in tiles])))

print(sum([sum(row) for row in tiles]))
