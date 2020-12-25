#!/usr/bin/python

class Space(object):
    def __init__(self):
        self.active = {}
        self.minx = 0
        self.maxx = 0
        self.miny = 0
        self.maxy = 0
        self.minz = 0
        self.maxz = 0
        self.minw = 0
        self.maxw = 0
    
    def get(self,x,y,z,w):
        return w in self.active and z in self.active[w] and y in self.active[w][z] and x in self.active[w][z][y]
    
    def count_(self, d):
        if isinstance(d, int):
            return 1
        return sum([self.count_(dd) for dd in d.values()])

    def count(self):
        return self.count_(self.active)
    
    def on(self,x,y,z,w):
        if x < self.minx:
            self.minx = x
        if x > self.maxx:
            self.maxx = x
        if y < self.miny:
            self.miny = y
        if y > self.maxy:
            self.maxy = y
        if z < self.minz:
            self.minz = z
        if z > self.maxz:
            self.maxz = z
        if w < self.minw:
            self.minw = w
        if w > self.maxw:
            self.maxw = w
    
        if w not in self.active:
            self.active[w] = {}
        if z not in self.active[w]:
            self.active[w][z] = {}
        if y not in self.active[w][z]:
            self.active[w][z][y] = {}
        if x not in self.active[w][z][y]:
            self.active[w][z][y][x] = 1
    
    def off(self,x,y,z,w):
        if get(x,y,z,w):
            self.active[w][z][y].remove(x)

def step(g):
    ng = Space()
    for w in range(g.minw - 1, g.maxw + 2):
        for z in range(g.minz - 1, g.maxz + 2):
            for y in range(g.miny - 1, g.maxy + 2):
                for x in range(g.minx - 1, g.maxx + 2):
                    an = 0
                    for ow in [w - 1, w, w + 1]:
                        for oz in [z - 1, z, z + 1]:
                            for oy in [y - 1, y, y + 1]:
                                for ox in [x - 1, x, x + 1]:
                                    if (ow != w or ox != x or oy != y or oz != z) and g.get(ox, oy, oz, ow):
                                        an += 1
                    if g.get(x,y,z,w):
                        if an == 2 or an == 3:
                            ng.on(x,y,z,w)
                    else:
                        if an == 3:
                            ng.on(x,y,z,w)
    return ng
        

##########################################################################

with open('start.txt') as fh:
    lines = fh.readlines()

g = Space()

for y in range(len(lines)):
    for x in range(len(lines[y].strip())):
        if lines[y][x] == '#':
            g.on(x,y,0,0)

print('%d: %d' % (0, g.count()))
for s in range(1,10):
    g = step(g)
    print('%d: %d' % (s, g.count()))
