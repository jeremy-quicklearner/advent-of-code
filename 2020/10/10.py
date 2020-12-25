#!/usr/bin/python

with open('adapters.txt') as fh:
    lines = fh.readlines()

nums = [int(l.strip()) for l in lines]
nums.append(0)
nums.append(max(nums) + 3)
nums.sort()

diffs = [None,0,0,0]

for idx in range(1,len(nums)):
    diffs[nums[idx]-nums[idx-1]] += 1

print(diffs[1] * diffs[3])

dp = {0:1}
for num in nums[1:]:
    acc = 0
    if num - 3 in dp:
        acc += dp[num - 3]
    if num - 2 in dp:
        acc += dp[num - 2]
    if num - 1 in dp:
        acc += dp[num - 1]

    if acc == 0:
        print('UH OH')
    dp[num] = acc

print(dp[max(nums)])
