# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

out=[]
for _ in xrange(int(raw_input())):
    s = raw_input()
    out.append(re.sub(" \|\| "," or ",re.sub(" \&\& "," and ",s)))
#print "-"*30
for _ in out:
    print _