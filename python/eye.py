import numpy

numpy.set_printoptions(sign=" ")
print numpy.eye(*(map(int,raw_input().split())),k=0,dtype=float)
