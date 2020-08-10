from itertools import groupby

data = '1222311'

print ( " ".join([ "(" + ", ".join( [k,str(len(list(g)))] ) + ")" for [k, g] in groupby(data) ]) )


print(*[(len(list(c)), int(k)) for k, c in groupby(data)])