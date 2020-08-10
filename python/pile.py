#!/usr/bin/pyton
def p(n):
    #print (n)
    last_pile = n[0] if n[0] > n[-1] else n[-1]
    for _ in range(len(n)):
        #print (last_pile, n)
        c=[ [last_pile,-2], [n[0],0], [n[-1],-1]]
        c.sort(key=lambda x: x[0],reverse=True)
        #print (c)
        if c[-1][-1] == -2 : 
            return "No"
        elif c[0][-1] == -2:
            last_pile = n.pop(c[1][-1])
        else: 
            last_pile = n.pop(c[-1][1])
    return "Yes"

for _ in xrange(int(raw_input())):
    raw_input()
    #print (p(map(int, raw_input().split()))
