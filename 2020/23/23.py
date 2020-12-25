#!/usr/bin/python

class Cup(object):
    def __init__(self, label):
        self.label = label
        self.prev = None
        self.next = None

def game(max, turns):
    labels = [int(i) for i in list('186524973')] + range(10,max + 1)
    cups = {}
    cup1 = Cup(labels[0])
    prev = cup1
    
    for label in labels[1:]:
        cup = Cup(label)
        prev.next = cup
        cup.prev = prev
    
        prev = cup
        cups[label] = cup
    
    cup1.prev = prev
    prev.next = cup1
    cups[1] = cup1

    currentcup = cups[1]
    for turn in range(turns):
    
        startcup = currentcup.next
        endcup = startcup.next.next
        endcup.next.prev = startcup.prev
        startcup.prev.next = endcup.next
        picked = [startcup.label, startcup.next.label, startcup.next.next.label]
    
        destlabel = currentcup.label - 1
        if destlabel == 0:
            destlabel = max
        while destlabel in picked:
            destlabel -= 1
            if destlabel == 0:
                destlabel = max
    
        destcup = cups[destlabel]
        endcup.next = destcup.next
        destcup.next.prev = endcup
        destcup.next = startcup
        startcup.prev = destcup
    
        currentcup = currentcup.next
    
        if turn and turn % 1000000 == 0:
            print('turn ' + str(turn))
    
    return cups

cups = game(9,100)
out = []
cup = cups[1].next
while cup.label != 1:
    out.append(cup.label)
    cup = cup.next
print(''.join([str(i) for i in out]))

cups = game(1000000,10000000)
print(cups[1].next.label * cups[1].next.next.label)
