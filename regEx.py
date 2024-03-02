# https://www.w3schools.com/python/python_regex.asp
import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

txt = "The rain in Spain 12"

# print(re.findall("[a-m]", txt))
# print(re.findall("\\d", txt))
# print(re.findall("S...n", txt))

# x = re.findall("ai", txt)
# print(x)

# Exactly the specified number of occurrences
# print(re.findall("r.{2}n", txt))

# Either or
# print(re.findall("rain|drain", txt))

# *	Zero or more occurrences	"he.*o"
# import re
# txt = "heo planet"
# x = re.findall("he.*o", txt)
# print(x)

# +	One or more occurrences	"he.+o"
# import re
# txt = "helo planet"
# x = re.findall("he.+o", txt)
# print(x)

# ?	Zero or one occurrences	"he.?o"
# import re
# txt = "heo planet"
# x = re.findall("he.?o", txt)
# print(x)

# SEARCH
# txt = "The rain in Spain"
# x = re.search("\\s", txt)
# print("The first white-space character is located in position:", x.start())

# x = re.search("Portugal", txt)
# print(x)

# SPLIT
# txt = 'The rain in Spain'
# x = re.split('\\s', txt)
# print(x)

# txt = 'The rain in Spain'
# x = re.split('\\s', txt, 1)
# print(x)

txt = 'The rain in Spain'
# x = re.sub('\\s', '9', txt)
# print(x)

# x = re.sub('\\s', '9', txt, 2)
# print(x)

# x = re.search('ai', txt)
# print(x)

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
x = re.search(r'\bS\w+', txt)
print(x.span())
print(x.string)
print(x.group())




