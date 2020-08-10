raw_input()
a=map(int,raw_input().split())
print all([ x>0 for x in a ]) and any( [ str(x)[:int(len(str(x))/2)]==(str(x)[::-1])[:-int(len(str(x))/2)] for x in a ] )