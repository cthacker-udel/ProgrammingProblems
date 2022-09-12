
def find_comb_noncontig(arr: int, t: int, k: int) -> int:
    _range = [t - k, t + k]
    combos = []
    combo_length = 1
    while combo_length < len(arr):
        pass


if __name__ == '__main__':
    find_comb_noncontig([-4, 2, 1, 6, 4, -3, -1], 5, 2)
