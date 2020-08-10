from collections import namedtuple;
sum , n, student = 0 , int(raw_input()) , namedtuple('Student',raw_input())
for i in range(n):
    ri  = raw_input().split() 
    sum+= int(student(ri[0],ri[1],ri[2],ri[3]).MARKS)
print "%.2f" % (sum/float(n))