#!/usr/bin/python

with open('bus.txt') as fh:
    lines = fh.readlines()

ts = int(lines[0].strip())

ls = lines[1].strip().split(',')

ls = [ int(n) for n in ls if n != 'x' ]
ls = [(n, ts % n - n) for n in ls]
print(ls)

ls = lines[1].strip().split(',')
els = [e for e in enumerate(ls) if e[1] != 'x']
els = [(i,int(n)) for (i,n) in els]

lastconvergence = 0
period = 1
for e in els:
    print('USING PERIOD %d AND INCORPORATING TERM ' % period + str(e))
    k = lastconvergence
    convergences = []
    while len(convergences) < 2:
        works = True
        (i,m) = e
        if (-k % m) == i % m:
            print('CONVERGENCE AT %d' % k)
            convergences.append(k)
        k += period
    period = convergences[1] - convergences[0]
    lastconvergence = convergences[0]
