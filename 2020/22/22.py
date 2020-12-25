#!/usr/bin/python
import copy

with open('cards.txt') as fh:
    lines = fh.readlines()

lines = ''.join(lines)
deck1, deck2 = lines.split('\n\n')
deck1 = deck1.strip().split('\n')[1:]
deck2 = deck2.strip().split('\n')[1:]
deck1 = [int(v) for v in deck1]
deck2 = [int(v) for v in deck2]

while deck1 and deck2:
    play1 = deck1[0]
    play2 = deck2[0]
    deck1 = deck1[1:]
    deck2 = deck2[1:]

    if play1 > play2:
        deck1 += [play1, play2]
    elif play2 > play1:
        deck2 += [play2, play1]
    else:
        print('UH OH')

win = deck1 if deck1 else deck2
print(sum([i*v for i,v in enumerate(reversed(win), 1)]))


lines = ''.join(lines)
deck1, deck2 = lines.split('\n\n')
deck1 = deck1.strip().split('\n')[1:]
deck2 = deck2.strip().split('\n')[1:]
deck1 = [int(v) for v in deck1]
deck2 = [int(v) for v in deck2]

def rcombat(d1, d2, g):
    sofar = {}
    r = 0
    while(d1 and d2):
        r += 1
        
        play1 = d1[0]
        play2 = d2[0]
        d1 = d1[1:]
        d2 = d2[1:]

        if play1 <= len(d1) and play2 <= len(d2):
            # winner of round
            winner = rcombat(copy.copy(d1[:play1]), copy.copy(d2[:play2]), g+1)[0]

        elif play1 > play2:
            winner = 1
        elif play2 > play1:
            winner = 2
        else:
            print('UH OH')

        if winner == 1:
            d1 += [play1, play2]
        elif winner == 2:
            d2 += [play2, play1]
        else:
            print('UH OH')

        if str(d1) + '|' + str(d2) in sofar:
            # p1 wins game
            return (1,0)
        sofar[str(d1) + '|' + str(d2)] = 1

    res = sum([i*v for i,v in enumerate(reversed(d1 if d1 else d2), 1)])
    return (1,res) if d1 else (2,res)


print(rcombat(deck1, deck2, 1)[1])
