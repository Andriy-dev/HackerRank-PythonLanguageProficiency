import numpy

''' print floor ceil and rint '''

#numpy.set_printoptions(sign=" ")
a=numpy.array(map(float,raw_input().split()))

print "{}\n{}\n{}".format(*[f(a) for f in [ numpy.floor,numpy.ceil,numpy.rint])