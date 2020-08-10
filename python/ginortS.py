import re

s=raw_input()
print ''.join(sorted(re.findall('[a-z]{1}',s)))+''.join(sorted(re.findall('[A-Z]{1}',s)))+''.join(sorted(re.findall('[13579]{1}',s)))+''.join(sorted(re.findall('[02468]{1}',s)))