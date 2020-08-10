import os
import random
import re
import sys
import datetime;

# Complete the time_delta function below.
def time_delta(t1, t2):
 
    t1o = datetime.datetime.strptime(" ".join(t1.split()[:5]), '%a %d %b %Y %H:%M:%S')
    t2o = datetime.datetime.strptime(" ".join(t2.split()[:5]), '%a %d %b %Y %H:%M:%S')

    print t1o
    print t2o

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        t1 = raw_input()

        t2 = raw_input()

        delta = time_delta(t1, t2)

       #fptr.write(delta + '\n')

    #fptr.close()
