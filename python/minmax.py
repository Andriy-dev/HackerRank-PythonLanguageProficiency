import numpy

# array=numpy.array([map(int,raw_input().split()) for x in xrange(map(int,raw_input().split())[0])])

# print array
# min1=numpy.min(array,axis = 1)
# print min1
# print numpy.max(min1)


print numpy.max( numpy.min(numpy.array([map(int,raw_input().split()) for x in xrange(map(int,raw_input().split())[0])]),axis = 1) )
