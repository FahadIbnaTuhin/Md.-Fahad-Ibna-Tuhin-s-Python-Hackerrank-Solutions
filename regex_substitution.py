import re

# (&&|\|\|): This part is a group that matches either '&&' or '||'. The | is the alternation operator, meaning "or."
# So, it matches either '&&' or '||'.
pattern = r"(?<= )(&&|\|\|)(?= )"
replacement = lambda x: "and" if x.group() == "&&" else "or"

inp = []

for _ in range(int(input())):
    print(re.sub(pattern, replacement, input()))

print(*inp, sep='\n')


# LESSON
# def sequare(match):
#     number = int(match.group(0))
#     return str(number ** 2)
# print(re.sub(r'\d+', sequare, '1 2 3 4 5 6 7'))

# html = """
# <head>
# <title>HTML</title>
# <object type="application/x-flash"
#   data="your-file.swf"
#   width="0" height="0">
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# """
# print(re.sub("(<!--.*?-->)", "", html))

