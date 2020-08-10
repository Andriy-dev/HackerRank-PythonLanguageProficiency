import numpy

print numpy.prod(numpy.sum(numpy.array([ map(int,raw_input().split()) for x in xrange(map(int,raw_input().split())[0]) ])
,axis=0))