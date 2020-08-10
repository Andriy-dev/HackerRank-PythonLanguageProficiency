from itertools import product

def f(elements,m):
    return sum(map(lambda x: pow(x,2),elements))%m

[k,m]=map(int,raw_input().split()) 
numbers=[list(set(map(int, (raw_input().split()[1:] )))) for _ in range(k)]

print max(f(x,m) for x in product(*numbers))


