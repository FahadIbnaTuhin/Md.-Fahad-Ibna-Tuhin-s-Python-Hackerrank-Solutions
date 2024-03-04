import re

# group()
# A group() expression returns one or more subgroups of the match

# m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# print(m.group(0))     # The entire match
'username@hackerrank.com'
# print(m.group(1))       # The first parenthesized subgroup.
# 'username'
# print(m.group(2))       # The second parenthesized subgroup.
# 'hackerrank'
# print(m.group(3))       # The third parenthesized subgroup.
# 'com'
# print(m.group(1, 2, 3))   # Multiple arguments give us a tuple.
# ('username', 'hackerrank', 'com')
# print(m.groups())
# A groups() expression returns a tuple containing all the subgroups of the match.


# m = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@hackerrank.com')
# print(m.groups())
# ('username', 'hackerrank', 'com')

# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup
# name.
m = re.match(r'(?P<username>\w+)@(?P<mailserver>\w+)\.(?P<domain>\w+)', 'myname@hackerrank.com')
print(m.groupdict())
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
