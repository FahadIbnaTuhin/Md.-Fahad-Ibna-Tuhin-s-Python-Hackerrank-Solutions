import re
from email.utils import parseaddr, formataddr

for _ in range(int(input())):
    mail = parseaddr(input())
    if re.match(r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$', mail[1]):
        print(formataddr(mail))


# ^: Asserts the start of the string.
# [a-z]: Matches a lowercase letter at the beginning of the email address.
# [\w\-\.]+: Matches one or more word characters (\w includes letters, digits, and underscores), hyphens (\-), or dots
# (\.). This part represents the local part of the email address (before the '@' symbol).
# @: Matches the '@' symbol.
# [a-z]+: Matches one or more lowercase letters. This represents the domain name (after the '@' symbol).
# \.: Matches the dot ('.') after the domain name.
# [a-z]{1,3}: Matches between 1 and 3 lowercase letters. This represents the top-level domain (TLD), like '.com' or
# '.org'. $: Asserts the end of the string.
