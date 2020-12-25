#!/usr/bin/python
import re

with open('pass.txt') as fh:
    lines = fh.readlines()

raw = ''.join(lines)

passes = raw.split('\n\n')
for passp in passes:
    fields = re.split(r'\s', passp )
    dict = {}
    for field in fields:
        kv = field.split(':')
        if len(kv) != 2:
            pass
        else:
            dict[kv[0].strip()] = kv[1].strip()

    valid = True
    for req in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if req not in dict:
            valid = False
    if valid:
        if int(dict['byr']) < 1920 or int(dict['byr']) > 2002:
            continue
        if int(dict['iyr']) < 2010 or int(dict['iyr']) > 2020:
            continue
        if int(dict['eyr']) < 2020 or int(dict['eyr']) > 2030:
            continue

        h = dict['hgt']
        if h[-2:] == 'cm':
            hn = int(h[:-2])
            if hn < 150 or hn > 193:
                continue
        elif h[-2:] == 'in':
            hn = int(h[:-2])
            if hn < 59 or hn > 76:
                continue
        else:
            continue

        if not re.match(r'^#[0-9a-f]{6}$', dict['hcl']):
            continue
        if dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue

        if not re.match(r'^[0-9]{9}$', dict['pid']):
            continue

        print('VALID')
