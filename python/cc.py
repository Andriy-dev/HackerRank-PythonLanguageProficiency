'''
Validation of credit card numbers

► It must start with a 4 , 5  or 6. ------ok
► It must contain exactly 16 digits. ------ok
► It must only consist of digits (0-9). ------ok
► It may have digits in groups of 4, separated by one hyphen "-".  ------ok
► It must NOT use any other separator like ' ' , '_', etc. ------ok
► It must NOT have 4 or more consecutive repeated digits.

Negative lookahead /foo(?!bar)/

^[456]\d{3}(?P<separator>-?)\d{4}(?P=separator)\d{4}(?P=separator)\d{4}$

^((?P<f0>[456])(?!(?P=f0){3}))
((?P<s0>\d)(?!(?P=s0){2}-?(?P=s0)))
((?P<t0>\d)(?!(?P=t0)-?(?P=t0){2}))
((?P<fo0>\d)(?!-?(?P=fo0){3}))
(?P<separator>-?)
((?P<f1>\d)(?!(?P=f1){3}))
((?P<s1>\d)(?!(?P=s1){2}-?(?P=s1)))
((?P<t1>\d)(?!(?P=t1)-?(?P=t1){2}))
((?P<fo1>\d)(?!-?(?P=fo1){3}))(?P=separator)
((?P<f2>\d)(?!(?P=f2){3}))
((?P<s2>\d)(?!(?P=s2){2}-?(?P=s1)))
((?P<t2>\d)(?!(?P=t2)-?(?P=t1){2}))
((?P<fo2>\d)(?!-?(?P=fo2){3}))
(?P=separator)
((?P<f3>\d)(?!(?P=f3){3}))
\d{3}$
'''

import re

pattern=r'^((?P<f0>[456])(?!(?P=f0){3}))((?P<s0>\d)(?!(?P=s0){2}-?(?P=s0)))((?P<t0>\d)(?!(?P=t0)-?(?P=t0){2}))((?P<fo0>\d)(?!-?(?P=fo0){3}))(?P<separator>-?)((?P<f1>\d)(?!(?P=f1){3}))((?P<s1>\d)(?!(?P=s1){2}-?(?P=s1)))((?P<t1>\d)(?!(?P=t1)-?(?P=t1){2}))((?P<fo1>\d)(?!-?(?P=fo1){3}))(?P=separator)((?P<f2>\d)(?!(?P=f2){3}))((?P<s2>\d)(?!(?P=s2){2}-?(?P=s1)))((?P<t2>\d)(?!(?P=t2)-?(?P=t1){2}))((?P<fo2>\d)(?!-?(?P=fo2){3}))(?P=separator)((?P<f3>\d)(?!(?P=f3){3}))\d{3}$'

for i in xrange(int(raw_input())):
    if re.match(pattern,raw_input()):
        print "Valid"
    else:
        print "Invalid"
