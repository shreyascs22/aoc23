import time
from functools import reduce

t1 = time.time()
items = open('q5.txt').read().split('\n\n')
seeds = items[0]
maps = items[1:]

def lookup(val, m):
    ranges = m.split('\n')[1:]
    for r in ranges:
        dst, src, n = map(int, r.split())
        if src <= val < src+n:
            return val-src+dst
    else: return val
print(min(reduce(lookup, maps, int(s)) for s in seeds.split()[1:]))
t2 = time.time()
print(t2-t1)