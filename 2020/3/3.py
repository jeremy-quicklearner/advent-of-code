#!/usr/bin/python3

with open('map.txt') as fh:
    lines = fh.readlines()

lines = [line.strip() for line in lines]
def get(x, y):
    l = lines[y]
    c = l[x % len(lines[0])]
    return {
        '.':0,
        '#':1
    }[c]

x = 0
y = 0
acc = 0
while y < len(lines) - 1:
    x += 1
    y += 2
    acc += get(x,y)
print(acc)
