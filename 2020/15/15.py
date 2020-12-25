#!/usr/bin/python

with open('start.txt') as fh:
    lines = fh.readlines()

start = lines[0].strip().split(',')
start = [int(s) for s in start]

turn = 0
last = {}
prev = 0

for i in range(len(start)):
    if i + 1 != len(start):
        last[start[i]] = turn
    prev = start[i]
    turn += 1
    print(start[i])

while turn < 30000000:
    if prev not in last:
        last[prev] = turn - 1
        prev = 0
        turn += 1
    else:
        lastprev = last[prev]
        last[prev] = turn - 1
        prev = turn - lastprev - 1
        turn += 1
    if turn % 1000000 == 0:
        print('%d: %d' % (turn, prev))
