from typing import List


def two_sum(a: List[int], x):
    """
    O(n lg n) implementation of two-sum

    Args:
        a (List[int]): _description_
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    a = sorted(a)
    i = len(a) - 1
    j = 0
    while i != j and j < i:
        if a[i] + a[j] < x:
            j += 1
        elif a[i] + a[j] > x:
            i -= 1
        else:
            print(a[i], a[j])
            return True
    return False


if __name__ == '__main__':
    arr = [1, 5, 4, 10, 2, 3]
    _sum = 11
    print(two_sum(arr, _sum))
