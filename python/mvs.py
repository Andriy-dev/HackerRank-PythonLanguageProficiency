#from __future__ import print_function
import numpy
from functools import partial

'''
First, print the mean. 
Second, print the var. 
Third, print the std.
'''
numpy.set_printoptions(precision=8)
array=numpy.array([ map(int,raw_input().split()) for _ in xrange(map(int,raw_input().split())[0])])

# print numpy.mean(array,axis=1)
# print numpy.var(array,axis=0)
# print numpy.std(array)

#b=[map(x,array) for x in [ partial(numpy.mean, axis=1), partial(numpy.var, axis=0), numpy.std ]]

#print [ x(array) for x in [ partial(numpy.mean, axis=1), partial(numpy.var, axis=0), partial(numpy.std, axis=None) ]]

print "{}\n{}\n{}\n".format(*[ x(array) for x in [ partial(numpy.mean, axis=1), partial(numpy.var, axis=0), partial(numpy.std, axis=None) ]])

#,lambda x: numpy.var(x,axis=0),lambda x: numpy.std(x,axis=None)