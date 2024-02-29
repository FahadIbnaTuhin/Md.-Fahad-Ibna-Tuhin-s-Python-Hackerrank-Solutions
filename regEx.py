# https://www.w3schools.com/python/python_regex.asp
import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

txt = "The rain in Spain 12"

# print(re.findall("[a-m]", txt))
# print(re.findall("\\d", txt))
# print(re.findall("S...n", txt))

# Zero or more occurrences
print(re.findall("T*e", txt))
# One or more occurrences
print(re.findall("T+e", txt))

# Zero or one
# print(re.findall("S?n", txt))

# Exactly the specified number of occurrences
# print(re.findall("r.{2}n", txt))

# Either or
# print(re.findall("rain|drain", txt))

