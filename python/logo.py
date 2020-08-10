#!/usr/bin/python

import math
import os
import random
import re
import sys
import string
from collections import Counter

if __name__ == '__main__':
    #s = raw_input()
    s = 'aabbbccde'
    c = Counter(s)
    print ("\n".join([" ".join([x,str(y)]) for x,y in sorted([ [x,c[x]] for x in c ],key=lambda x: 10000*x[1]+(25-string.lowercase.index(x[0])),reverse=True)[0:3]]))

    