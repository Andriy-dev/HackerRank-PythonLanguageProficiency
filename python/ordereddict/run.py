# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

od=OrderedDict()

n=int(raw_input())
for _ in xrange(n):

    input=raw_input().split()
    name=" ".join(input[:-1])
    price=int(input[-1])


    #print name,price
    if name in [x[0] for x in od.items()]:
        od[name]+=price
    else:
        od[name]=price
        
for i in od.items():
    print i[0],i[1]
