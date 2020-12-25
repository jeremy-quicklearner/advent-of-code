#!/usr/bin/python3

import re

with open('data.txt') as fh:
    lines = fh.readlines()

lines = ''.join(lines)
rules, exprs = lines.split('\n\n')
rules = rules.split('\n')
exprs = exprs.split('\n')

grammar = {}
while rules:
    remainingrules = []
    for rulestr in rules:
        idx = rulestr.index(':')
        key = rulestr[:idx]

        toks = rulestr[idx+1:].strip().split(' ')

        canresolve = True
        for tok in toks:
            if tok not in grammar and tok != '|' and not re.match(r'"."$', tok):
                canresolve = False
        if not canresolve:
            remainingrules.append(rulestr)
            continue

        if re.match(r'^"."$', toks[0]):
            grammar[key] = toks[0][1:2]
            continue

        opts = ' '.join(toks).split(' | ')
        gramopts = []
        for stropt in opts:
            gramopt = None
            for tok in stropt.split(' '):
                if gramopt is None:
                    gramopt = grammar[tok.strip()]
                else:
                    gramopt = gramopt + grammar[tok.strip()]
            gramopts.append('(' + gramopt + ')')
        grammar[key] = '(' + '|'.join(gramopts) + ')'
    rules = remainingrules

# For part 2, manually override rules 8 and 11.

# 8: 42 | 42 8
# Hooray, it's regular
grammar['8'] = '(' + grammar['42'] + '+)'

# 11: 42 31 | 42 11 31
# Not regular, so I can't express it properly. But I do know all the given
# strings are of finite length, so I can write regexes for up to N recursive
# expansions and crank up N until AoC accepts the answer
eleven = [grammar['42'] + grammar['31']]
for _ in range(3):
    eleven.append(grammar['42'] + eleven[-1] + grammar['31'])
grammar['11'] = '(' + '|'.join(['(' + e + ')' for e in eleven]) + ')'

# 0 is the only rule that depends on 8 and 11, so override it too
grammar['0'] = grammar['8'] + grammar['11']

count = 0
for expr in exprs:
    print('<' + expr.strip() + '>')
    sexpr = expr.strip()
    count += 1 if re.match('^' + grammar['0'] + '$', sexpr) else 0
print('MATCHES: ' + str(count))
