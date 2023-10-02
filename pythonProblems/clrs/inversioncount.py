def inversion_count(arr):
    print(arr)
    i = 0
    j = len(arr) - 1
    total = 0
    while i <= j:
        if arr[i] > arr[j]:
            print((arr[i], arr[j]))
            total += 1
            j -= 1
        else:
            j = len(arr) - 1
            i += 1
    return total


def number_of_inversions(arr):
    if len(arr) <= 1:
        return 0
    return number_of_inversions(arr[:len(arr) // 2]) + number_of_inversions(arr[len(arr) // 2:]) + inversion_count(arr)


if __name__ == '__main__':
    glob_arr = [2, 3, 8, 6, 1]
    print(number_of_inversions(glob_arr))
