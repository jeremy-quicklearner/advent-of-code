#!/usr/bin/python

with open('notes.txt') as fh:
    lines = fh.readlines()

lines = ''.join(lines)

rulestrs, your, nearby = lines.split('\n\n')

rulestrs = rulestrs.split('\n')
rules = {}
for rulestr in rulestrs:
    srulestr = rulestr.strip()
    idx = srulestr.index(':')
    name = srulestr[:idx]
    constraintstr = srulestr[idx+2:]

    idx = constraintstr.index(' or ')
    range1 = constraintstr[:idx]
    range2 = constraintstr[idx+4:]

    idx = range1.index('-')
    min1 = range1[:idx]
    max1 = range1[idx+1:]

    idx = range2.index('-')
    min2 = range2[:idx]
    max2 = range2[idx+1:]

    rules[name] = {'min1':int(min1),'max1':int(max1),'min2':int(min2),'max2':int(max2)}

your = your.split('\n')[1]
nearby = nearby.split('\n')[1:-1]


invalid = 0
validnearby = []
for ticket in nearby:
    valid = True
    for fieldstr in ticket.strip().split(','):
        field = int(fieldstr)
        found = False
        for name in rules:
            c = rules[name]
            if (field >= c['min1'] and field <= c['max1']) or (field >= c['min2'] and field <= c['max2']):
                found = True
                break
        if not found:
            valid = False
            invalid += field
    if valid:
        validnearby.append(ticket)

print(invalid)

possiblenames = [rules.keys() for _ in validnearby[0].strip().split(',')]
for ticket in validnearby:
    for idx, fieldstr in enumerate(ticket.strip().split(',')):
        field = int(fieldstr)
        for name in possiblenames[idx]:
            c = rules[name]
            if not ((field >= c['min1'] and field <= c['max1']) or (field >= c['min2'] and field <= c['max2'])):
                possiblenames[idx].remove(name)

passneeded = 1
while passneeded:
    passneeded = 0
    for pnames in possiblenames:
        if len(pnames) == 1:
            for otherpnames in possiblenames:
                if pnames is not otherpnames and pnames[0] in otherpnames:
                    passneeded = 1
                    otherpnames.remove(pnames[0])

final = {}
for pnames, field in zip(possiblenames, your.strip().split(',')):
    final[pnames[0]] = int(field)

filt = {k:v for k,v in final.items() if 'departure' in k}
acc = 1
for v in filt.values():
    acc = acc * int(v)

print(acc)
