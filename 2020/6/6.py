#!/usr/bin/python

with open('data.txt') as fh:
    lines = fh.readlines()

big = ''.join(lines)
groups = big.split('\n\n')

acc = 0
for group in groups:
    people = group.split('\n')

    #found = []
    #for c in 'abcdefghijklmnopqrstuvwxyz':
    #    for person in people:
    #        if c in person and c not in found:
    #            found.append(c)

    found = 'abcdefghijklmnopqrstuvwxyz'
    for c in 'abcdefghijklmnopqrstuvwxyz':
        for person in people:
            if c not in person:
                found = found.replace(c,'')

    acc += len(found)
    

print(acc)
