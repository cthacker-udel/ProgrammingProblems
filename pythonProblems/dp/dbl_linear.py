from typing import List


def dbl_linear(n: int) -> List[int]:
    """

    Args:
        n (_type_): _description_
    """
    seq = [1]
    ind = 0
    gen_numbers = 1
    y_array = []
    z_array = []
    while len(seq) < n:
        for eachnum in seq[ind: ind + gen_numbers]:
            y_array.append(2 * eachnum + 1)
        for eachnum in seq[ind: ind + gen_numbers]:
            z_array.append(3 * eachnum + 1)
        ind += gen_numbers
        gen_numbers = ind + (gen_numbers * 2) - ind
        seq.extend(y_array)
        seq.extend(z_array)
        y_array = []
        z_array = []
    return seq[u]
    # u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]


if __name__ == '__main__':
    u = 10
    dbl_linear(u)
