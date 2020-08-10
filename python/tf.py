import numpy

''' transpose and flatten exercise from hackerrank '''

a=numpy.array([map(int,raw_input().split()) for _ in xrange(map(int,raw_input().split())[0])])
print '{}\n{}'.format(a.transpose(),a.flatten())

