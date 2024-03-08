from html.parser import HTMLParser


class Html(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")


parser = Html()
# parser.feed('<head><title>HTML</title></head><object type="application/x-flash" data="your-file.swf" width="0"'
#     ' height="0"><!-- <param name="movie" value="your-file.swf" /> --><param name="quality" value="high"/></object>')

s = ''
for _ in range(int(input())):
    inp = input()
    s += inp.rstrip() + '\n'

parser.feed(s)
