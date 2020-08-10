from __future__ import print_function
import re

block_pattern = '([^{]+{(?P<body>[^{]*)})'
color_pattern = r"(#[0-9A-Fa-f]{6}(?![0-9A-Fa-f]))|(#[0-9A-Fa-f]{3}(?![0-9A-Fa-f]))"

txt=str()

for i in xrange(int(raw_input())):
    txt="".join([txt,raw_input()])

for i in re.findall(block_pattern,txt):
    [ print("".join(x)) for x in re.findall(color_pattern,i[1]) ]

