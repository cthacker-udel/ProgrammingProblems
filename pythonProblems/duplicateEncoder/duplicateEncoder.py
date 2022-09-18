def duplicate_encode(word):
    word = word.lower()
    return ''.join(['(' if word.count(x) == 1 else ')' for x in word])


if __name__ == '__main__':
    print(duplicate_encode('Success'))
