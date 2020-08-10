import inspect

def outer():
    print "Outer function"
    x = 1
    def inner():
        print "Innter function",x
    inner()

outer()

print outer.__class__
print 

print inspect.getdoc(map)
