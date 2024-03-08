from html.parser import HTMLParser


class Result(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")


parser = Result()
# parser.feed("<html><head><title>HTML Parser - I</title></head>" +
# "<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")

for _ in range(int(input())):
    parser.feed(input().strip())

# LESSON: create a subclass and override the handler methods
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Found a start tag  :", tag)
#
#     def handle_endtag(self, tag):
#         print("Found an end tag   :", tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print("Found an empty tag :", tag)
# parser = MyHTMLParser()
# parser.feed("<html><head><title>HTML Parser - I</title></head>"
#             +"<body><h1>HackerRank</h1><br /></body></html>")
