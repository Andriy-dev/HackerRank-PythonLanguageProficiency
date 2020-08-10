import numpy

(n,m)=map(int,raw_input().split())

(A,B)=([],[])

for _ in xrange(n):
    A.append(map(int,raw_input().split()))
for _ in xrange(n):
    B.append(map(int,raw_input().split()))

a = numpy.array(A, int)
b = numpy.array(B, int)

print a+b

print a - b

print a * b

print a / b

print a % b

print a**b
