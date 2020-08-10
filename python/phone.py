'''
phone number validation
'''

from __future__ import print_function
import re


pattern=re.compile(r'^[789]\d{9}')

validation=list()

for i in xrange(int(raw_input())):
    validation.append('YES' if re.match(pattern,raw_input()) else 'NO')

[ print(x) for x in validation ]