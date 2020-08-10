import re
for i in xrange(int(raw_input())):
    print True if re.match('^(\+|-){0,1}\d+\.\d+$',raw_input()) else False
