#!/usr/bin/python

with open('er.txt', 'r') as fh:
    erstr = fh.read()

erarr = erstr.strip().split('\n')
nums = [int(i) for i in erarr]

assoc = {2020 - i : i for i in nums}

for i in nums:
    if i in assoc:
        print("Found %d * %d = %d" % (i, 2020 - i, i * (2020 - i)))

assoc = {}
for i in nums:
    for j in nums:
        assoc[2020 - (i + j)] = (i,j)

for i in nums:
    if i in assoc:
        print("Found %d * %d * %d = %d" % (i, assoc[i][0], assoc[i][1], i * assoc[i][1] * assoc[i][0]))
