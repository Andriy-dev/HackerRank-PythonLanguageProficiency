from functools import reduce
from fractions import gcd

numerators = list()
denumenators = list()

for i in xrange(int(raw_input())):
    numerator, denumenator = map(int,raw_input().split())
    numerators.append(numerator)
    denumenators.append(denumenator)

n = reduce(lambda x,y : x*y, numerators)
d = reduce(lambda x,y : x*y, denumenators)

print n/gcd(n,d),d/gcd(n,d)
