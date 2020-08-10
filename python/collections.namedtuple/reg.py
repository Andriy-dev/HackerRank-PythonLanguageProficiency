import re

ra=list()
for _ in xrange(int(raw_input())):
    ra.append(raw_input())
for i in xrange(len(ra)):
    try:
        re.compile(ra[i])
        print True
    except re.error:
        print False

