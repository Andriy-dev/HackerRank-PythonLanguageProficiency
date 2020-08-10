from collections import OrderedDict;

n = int(raw_input())
od = OrderedDict()

for _ in xrange(n):
    w = raw_input()
    try:
        od[w]+=1
    except KeyError:
        od[w]=1

#print len(od.keys())
#print [x[1] for x in od.items()]
print str(len(od.keys()))
print " ".join([str(x[1]) for x in od.items()])
