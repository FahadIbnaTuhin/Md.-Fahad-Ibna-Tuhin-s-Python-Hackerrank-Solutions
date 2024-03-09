# https://www.youtube.com/watch?v=zrpqyrFVbDw
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # Here element is the feed element of the input, The below line will find out all the childs.
    if len(elem.findall('.//')) > 0:
        level = level + 1
        if level >= maxdepth:
            maxdepth = level + 1
        for i in elem:  # It will pass all the child of the feed one by one
            depth(i, level)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
