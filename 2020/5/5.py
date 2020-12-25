#!/usr/bin/python

with open('passes.txt') as fh:
    lines = fh.readlines()

lines = [line.replace('B','1') for line in lines]
lines = [line.replace('F','0') for line in lines]
lines = [line.replace('R','1') for line in lines]
lines = [line.replace('L','0') for line in lines]
nums = [int(line,2) for line in lines]
print(max(nums))

missing = range(0,2**10)
missing = [seat for seat in missing if seat not in nums]
print(missing)
