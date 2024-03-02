# First learn Roman Numiral From Khan Jhan Youtube channel, then ask chatgpt
# for help, then solve. {0,3} applies only to the letter "I"

import re

pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

match_result = bool(re.match(pattern, input()))
print(str(match_result))
