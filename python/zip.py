#!/usr/bin/python

(stud,subj) = map(int,raw_input().split())
grades=list()
for _ in xrange(subj):
    grades+=[map(float,raw_input().split())]
for i in zip(*grades):
    print sum(i)/subj