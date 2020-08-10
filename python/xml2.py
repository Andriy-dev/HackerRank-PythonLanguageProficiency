import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    s=len(node.attrib)
    for x in node:
        if len(x)>0:
            s+=get_attr_number(x)
        else:
            s+=len(x.attrib)
    return s

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()

    print get_attr_number(root)