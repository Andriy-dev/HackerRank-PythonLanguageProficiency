from copy import deepcopy;

lines,columns = map(int,raw_input().split())

table=list()

for _ in xrange(lines):
    table.append(map(int,raw_input().split()))

attribute=int(raw_input())

#otable=deepcopy(table)

for l in sorted( table,key=(lambda x: x[attribute]) ):
    print " ".join(map(str,l))