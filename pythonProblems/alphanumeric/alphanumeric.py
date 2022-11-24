import string

def alphanumeric(password: str) -> bool:
    print('password = ', password)
    if len(password) == 0:
        return False
    else:
        return ' ' not in password and '_' not in password and '\n' not in password and '\t' not in password and len([x for x in string.punctuation if x in password]) == 0