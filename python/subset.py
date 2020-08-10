result=list()
for i in xrange(int(raw_input())):
    raw_input()
    a=map(int,raw_input().split())
    raw_input()
    b=map(int,raw_input().split())
    subset=True
    for x in a:
        try:
            b.remove(x)
        except ValueError:
            subset=False
            break
    result.append(subset)
for i in result:
    print i