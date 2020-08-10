import operator

def person_lister(f):
    def inner(people):
        people=[ [x[0],x[1],int(x[2]),x[3]] for x in people]
        people.sort(key=operator.itemgetter(2))
        #print people
        return [f(x) for x in people ]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))