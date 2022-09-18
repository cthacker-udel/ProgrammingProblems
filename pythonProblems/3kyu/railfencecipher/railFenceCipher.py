def encode_rail_fence_cipher(string, n):
    _ind = 0
    inc_ = True
    indexes = []
    times_ = 0
    for i in range(len(string)):  # O(mn^2)
        if times_ == n:
            inc_ = not inc_
            _ind += 2 if inc_ else -2
            times_ = 1
        indexes.append(_ind)
        _ind += 1 if inc_ else -1
        times_ += 1
    output = ''
    print(indexes)
    for i in range(n):
        for j in range(len(string)):
            if indexes[j] == i:
                output += string[j]
    return output


def decode_rail_fence_cipher(string, n):
    n_ = 2 * (n - 1)
    while (len(string) % n_ != 0):
        string = string + " "
    k = len(string) // n_
    top = []
    middles = []
    bottom = []
    substr = ''
    for i in range(len(string)):
        letter = string[i]
        substr += letter
        if not top and len(substr) == k:
            top.append(substr)
            substr = ''
        elif not bottom and len(substr) == k and i >= (len(string) - 6):
            bottom.append(substr)
            substr = ''
        elif top and len(substr) == (2*k):
            middles.append(substr)
            substr = ''
    curr_indexes = [0] + [0 for x in middles] + [0]
    parts = top + middles + bottom
    output = ''
    inc_ = True
    ind_ = 0
    while sum(curr_indexes) != len(string):
        output += parts[ind_][curr_indexes[ind_]]
        curr_indexes[ind_] += 1
        ind_ += 1 if inc_ else -1
        inc_ = True if ind_ == 0 else False if ind_ == len(
            curr_indexes) - 1 else inc_

    print(output)


if __name__ == '__main__':
    decode_rail_fence_cipher("WECRUOERDSOEERNTNEAIVDAC", 3)
