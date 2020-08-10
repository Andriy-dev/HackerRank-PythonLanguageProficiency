#!/usr/bin/python 

raw_input()
a=set(map(int,raw_input().split()))

for i in xrange(int(raw_input())):
    op=raw_input().split()[0]
    b=set(map(int,raw_input().split()))
    if op=='update':
        a|=b
    elif op=='intersection_update':
        a&=b
    elif op=='difference_update':
        a-=b
    elif op=='symmetric_difference_update':
        a^=b

print sum(a)
