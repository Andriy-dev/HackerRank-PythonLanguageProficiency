a = set(map(int,raw_input().split()))
ss = True
for _ in xrange(int(raw_input())):
    b = set(map(int,raw_input().split()))
    if not ( a.intersection(b) == b and len(a) > len(b) ):
        ss = False
print ss
        