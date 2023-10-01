import re


def lowercase_count(strng):
    return len(re.findall(r'[a-z]', strng))


print(lowercase_count('hello'))
