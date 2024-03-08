import re

s = input()
k = input()

pattern = re.compile(k)
r = pattern.search(s)

if not r:
    print("(-1, -1)")

while r:
    print(f"({r.start()}, {r.end() - 1})")
    r = pattern.search(s, r.start() + 1)


# LESSON
# Return the indices of the start and end of the substring matched by the group
# m = re.search(r'\d+', 'adsf7898asdf')
# print(m.end())  # 4
# print(m.start())  # 0
