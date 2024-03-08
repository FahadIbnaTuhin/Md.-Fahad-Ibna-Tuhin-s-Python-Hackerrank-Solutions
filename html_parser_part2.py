from html.parser import HTMLParser


class GetResult(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


parser = GetResult()
html_string = ''
for _ in range(int(input())):
    html_string += input().rstrip() + '\n'

parser.feed(html_string)
parser.close()

# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         if "\n" in data:
#             print("M Comment :", data)
#         else:
#             print("S Comment :", data)
#
#     def handle_data(self, data):
#         print("Data :", data)
#
#
# parser = MyHTMLParser()
# parser.feed("<!--HelloFu&^B]'?-->")
# parser.feed("<!--HelloFu&^B]'?\nFahad-->")
# parser.feed("<style>body { background-color: red; }</style>" +
#             "<script>console.log('Hello')</script>")
