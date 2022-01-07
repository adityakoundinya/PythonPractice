from z3 import *

# each block of code is identical, except for the parameters on lines 4, 5, and 15, so we cache these
lst = open('day24.txt', 'r').read().splitlines()
lst = [[int(y.split()[-1]) for y in [lst[i+4],lst[i+5],lst[i+15]]] for i in range(0,len(lst),18)]

def solve(max):
    s = Optimize()
    z = 0  # this is our running z, which has to be zero at the start and end
    v = 0  # this is the value from concatenating our digits
    for (i,[p,q,r]) in enumerate(lst):
        w = Int(f'w{i}')
        v = v * 10 + w
        s.add(And(w >= 1, w <= 9))
        z = If(z % 26 + q == w, z / p, z / p * 26 + w + r)
    s.add(z == 0)

    (s.maximize if max else s.minimize)(v)
    assert s.check() == sat
    return s.model().eval(v)

print(solve(True)) # part 1
print(solve(False)) # part 2
