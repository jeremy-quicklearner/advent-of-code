#!/usr/bin/python

with open('instr.txt') as fh:
    lines = fh.readlines()

sx = 0
sy = 0
wx = 10
wy = 1
d = 0

for instr in lines:
    letter = instr[0]
    num = int(instr.strip()[1:])

    #if letter == 'L':
    #    d = ( d + (num / 90) ) % 4
    #    continue

    #if letter == 'R':
    #    d = ( d - (num / 90) ) % 4
    #    continue

    #if letter == 'F':
    #    sx += [num, 0, -num, 0][d]
    #    sy += [0, num, 0, -num][d]
    #    continue

    #if letter == 'E':
    #    sx += num
    #    continue
    #if letter == 'N':
    #    sy += num
    #    continue
    #if letter == 'W':
    #    sx -= num
    #    continue
    #if letter == 'S':
    #    sy -= num
    #    continue

    if letter == 'L':
        while num :
            num -= 90
            dx = wx - sx
            dy = wy - sy

            wx = sx - dy
            wy = sy + dx
        continue

    if letter == 'R':
        while num :
            num -= 90
            dx = wx - sx
            dy = wy - sy

            wx = sx + dy
            wy = sy - dx
        continue

    if letter == 'F':
        dx = wx - sx
        dy = wy - sy
        while num:
            num -= 1
            wx += dx
            wy += dy
            sx += dx
            sy += dy
        continue

    if letter == 'E':
        wx += num
        continue
    if letter == 'N':
        wy += num
        continue
    if letter == 'W':
        wx -= num
        continue
    if letter == 'S':
        wy -= num
        continue
print(abs(sx) + abs(sy))
