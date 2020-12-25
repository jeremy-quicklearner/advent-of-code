#!/usr/bin/python3

with open('cs.txt') as fh:
    lines = fh.readlines()

def run(prog):
    visited = {}

    acc = 0
    pc = 0

    while pc not in visited:
        if pc == len(prog):
            print('Terminates with acc ' + str(acc))
            return True
        visited[pc] = 1

        opcode, arg = prog[pc].strip().split(' ')
        arg = int(arg)

        if opcode == 'nop':
            pc += 1
            continue

        if opcode == 'jmp':
            pc += arg
            continue

        if opcode == 'acc':
            acc += arg
            pc += 1
            continue

    print('Loops with acc ' + str(acc))

    return False

for idx in range(len(lines)):
    opcode, arg = lines[idx].strip().split(' ')
    if opcode == 'acc':
        print('Skipping acc')
        continue

    prog = lines.copy()
    if opcode == 'nop':
        prog[idx] = 'jmp ' + arg + '\n'
    elif opcode == 'jmp':
        prog[idx] = 'nop ' + arg + '\n'

    run(prog)
