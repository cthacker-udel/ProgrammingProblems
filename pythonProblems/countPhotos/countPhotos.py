
def count_photos(road):
    _ct = 0
    _left = 0
    _right = 0
    _i = 0
    _j = len(road) - 1
    while _i < len(road) or _j >= 0:
        if road[_i] == '.':
            _ct += _right
        elif road[_i] == '>':
            _right += 1

        if road[_j] == '.':
            _ct += _left
        elif road[_j] == '<':
            _left += 1
        _i += 1
        _j -= 1
    return _ct


if __name__ == '__main__':
    print(count_photos('.><.>>.<<'))
