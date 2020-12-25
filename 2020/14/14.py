#!/usr/bin/python3
import copy

with open('instr.txt') as fh:
    lines = fh.readlines()

mem = {}
mask = '000000000000000000000000000000000000'

for line in lines:
    if line[:4] == 'mask':
        mask = line.strip().split()[2]
    if line[:3] == 'mem':
        addr = int(line.strip().split(' ')[0].split('[')[1][:-1])
        val = int(line.strip().split(' ')[2])
        mval = ''.join([{'0':'0','1':'1','X':v}[m] for (m,v) in zip(mask,'{:036b}'.format(val))])
        mem[addr] = mval

print(sum([int(mem[addr],2) for addr in mem]))

mem = {}
mask = '000000000000000000000000000000000000'

def variants(maddr):
    if maddr.count('X') == 0:
        return [maddr]
    idx = maddr.index('X')
    variant0, variant1 = copy.copy(maddr), copy.copy(maddr)
    variant0[idx] = '0'
    variant1[idx] = '1'
    return variants(variant0) + variants(variant1)

for line in lines:
    if line[:4] == 'mask':
        mask = line.strip().split()[2]
    if line[:3] == 'mem':
        addr = int(line.strip().split(' ')[0].split('[')[1][:-1])
        val = int(line.strip().split(' ')[2])
        maddr = [{'0':a,'1':'1','X':'X'}[m] for (m,a) in zip(mask,'{:036b}'.format(addr))]
        for variant in variants(maddr):
            mem[int(''.join(variant),2)] = val


print(sum([mem[addr] for addr in mem]))
