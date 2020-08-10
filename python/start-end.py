import re

instring=raw_input()
pattern = re.compile(raw_input())

m = pattern.search(instring)
if m:
    while m:
        print (m.start(),m.end()-1)
        m = pattern.search(instring,m.end()-1)
else:
    print (-1,-1)