# https://www.youtube.com/watch?v=sjriwAxSKoU
import sys
import xml.etree.ElementTree as etree
from html.parser import HTMLParser


def get_attr_number(node):
    val = 0
    for child in node.iter():
        # print(i)
        # print(child.attrib)
        val += len(child.attrib)
    return val


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
