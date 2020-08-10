import numpy
n,m,p = map(int,raw_input().split())

# n lines/p columns
# m lines/p columns
 
print numpy.concatenate((numpy.array( [x for y in xrange(n) for x in [map(int,raw_input().split())] ]), numpy.array( [x for y in xrange(m) for x in [map(int,raw_input().split())] ])), axis = 0)