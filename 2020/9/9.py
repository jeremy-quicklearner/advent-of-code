#!/usr/bin/python

def twosum(list, target):
    for i in list:
        for j in list:
            if i != j and i + j == target:
                return True
    return False

with open('xmas.txt') as fh:
    lines = fh.readlines()

nums = [int(l.strip()) for l in lines]

idx = 25

while(True):
    last25 = nums[idx-25:idx]
    if twosum(last25, nums[idx]):
        idx += 1
    else:
        break

targetsum = nums[idx]

wstart = 0
wend = 1

while(True):
    cursum = sum(nums[wstart:wend+1])
    if cursum < targetsum:
        wend += 1
    elif cursum > targetsum:
        wstart += 1
    else:
        print("%d %d" % (wstart, wend))
        window = nums[wstart:wend+1]
        print(min(window) + max(window))
        break

    print(cursum)
