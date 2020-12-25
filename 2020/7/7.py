#!/usr/bin/python

class Bags(object):
    def __init__(self, colour, amount):
        self.colour = colour
        self.amount = amount

with open('rules.txt') as fh:
    lines = fh.readlines()

bags = {}

for line in lines:
    [outer, inner] = line.split(' bags contain ')
    inner = inner.split(',')
    innerbags = []
    for bagstr in inner:
        bag = bagstr.strip().split(' ')
        if bag[0] != 'no':
            amount = int(bag[0])
            colour = bag[1] + ' ' + bag[2]
            innerbags.append(Bags(colour, amount))
    bags[outer] = innerbags

passneeded = False
hasgold = ['shiny gold']

while True:
    for outercolour in bags:
        for innerbag in bags[outercolour]:
            if innerbag.colour in hasgold and outercolour not in hasgold:
                hasgold.append(outercolour)
                passneeded = True
    if not passneeded:
        break

    passneeded = False

print(len(hasgold) - 1)

def countBags(key):
    if len(bags[key]) == 0:
        return 1
    acc = 1
    for innerbag in bags[key]:
        acc += innerbag.amount * countBags(innerbag.colour)
    return acc

print(countBags('shiny gold') - 1)
