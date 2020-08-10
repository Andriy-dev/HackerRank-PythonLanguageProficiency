def wrapper(f):
    '''The given mobile numbers may have +91 , 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all. '''
    def fun(l):
        #print l
        l = [ "+91 " + " ".join([x[-10:-5],x[-5:]]) for x in l ]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l) 