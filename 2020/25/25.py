#!/usr/bin/python
doorpubkey = 9093927
cardpubkey = 11001876

mod = 20201227

v = 1
ls = 0
while True:
    ls += 1
    v = (v * 7) % mod
    if v == doorpubkey:
        otherkey = cardpubkey
        break
    if v == cardpubkey:
        otherkey = doorpubkey
        break
    
v = 1
for _ in range(ls):
    v = (v * otherkey) % mod
print(v)
