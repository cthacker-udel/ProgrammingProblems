def minflips(binstring):
    curr = '1'
    count = 0
    for eachchar in binstring:
        if eachchar == curr:
            count += 1
            curr = '0' if curr == '1' else '1'
    return count


if __name__ == '__main__':
    print(minflips('011000'))
