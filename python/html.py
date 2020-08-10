from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for attr in attrs:
            print "->"," > ".join(map(str,attr))

    def handle_endtag(self, tag):
        print "End   :", tag

    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for attr in attrs:
            print "->"," > ".join(map(str,attr))

parser = MyHTMLParser()
for _ in xrange(int(raw_input())):
    parser.feed(raw_input())