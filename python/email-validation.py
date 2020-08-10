from __future__ import print_function
import re

#valid=list()

for _ in xrange(int(raw_input())):
    (name,email) = raw_input().split()
    if re.match(r'.+',name) and re.match(r'^<[a-zA-Z-_\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$',email):
        print(" ".join([name,email]))
    
        #valid.append(" ".join([name,email]))
#[ print(x) for x in valid ] 