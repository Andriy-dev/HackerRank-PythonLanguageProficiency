import re
emails=list()

for _ in xrange(int(raw_input())):
    emails.append(raw_input())

print sorted(filter(lambda x: re.match(pattern,x) , emails))