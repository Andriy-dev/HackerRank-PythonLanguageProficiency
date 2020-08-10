from HTMLParser import HTMLParser

''' 
Sample input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

Sample output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high

'''


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print " ".join( ["->",attr[0],">",attr[1] ])

lines = int(raw_input())

parser = MyHTMLParser()

parser.feed(" ".join([raw_input() for _ in xrange(lines)]))

