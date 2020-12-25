#!/usr/bin/python

with open('passwd.txt') as fh:
    lines = fh.readlines()

for line in lines:
    toks = line.split()
    r = toks[0]
    c = toks[1][:-1]
    p = toks[2].strip()

    toks2 = r.split('-')

    min = toks2[0]
    max = toks2[1]

    i = p.count(c)

    #if i < int(min) or i > int(max):
    #    print(line.strip())
    
    cmin = (p[int(min) - 1] == c)
    cmax = (p[int(max) - 1] == c)

    if cmin != cmax:
        print('OK')
