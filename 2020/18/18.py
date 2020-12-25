#!/usr/bin/python
import re

with open('homework.txt') as fh:
    lines = fh.readlines()

exprs = [line.strip() for line in lines]

def evalNoParen(expr):
    sexpr = expr.strip()
    if re.match(r'^\d+$', sexpr):
        return int(sexpr)
    toks = sexpr.split(' ')
    if toks[-2] == '+':
        return evalNoParen(toks[-1]) + evalNoParen(' '.join(toks[:-2]))
    elif toks[-2] == '*':
        return evalNoParen(toks[-1]) * evalNoParen(' '.join(toks[:-2]))
    else:
        print('UH OH')

def evalNoParenWithPrec(expr):
    sexpr = expr.strip()
    if re.match(r'^\d+$', sexpr):
        return int(sexpr)
    toks = sexpr.split(' ')
    if '*' in toks:
        idx = toks.index('*')
        return evalNoParenWithPrec(' '.join(toks[:idx])) * evalNoParenWithPrec(' '.join(toks[idx+1:]))
    if '+' in toks:
        idx = toks.index('+')
        return evalNoParenWithPrec(' '.join(toks[:idx])) + evalNoParenWithPrec(' '.join(toks[idx+1:]))
    else:
        print('UH OH')

def eval(expr, prec):
    if '(' not in expr:
        return evalNoParenWithPrec(expr) if prec else evalNoParen(expr)
    depth = 1
    startidx = expr.index('(')
    idx = startidx
    while True:
        idx += 1
        if expr[idx] == '(':
            depth += 1
        elif expr[idx] == ')':
            depth -= 1
        if depth == 0:
            break
    endidx = idx

    return eval(expr[:startidx] + str(eval(expr[startidx+1:endidx], prec)) + expr[endidx+1:], prec)

sols = [eval(expr, False) for expr in exprs]
print(sum(sols))
sols = [eval(expr, True) for expr in exprs]
print(sum(sols))
