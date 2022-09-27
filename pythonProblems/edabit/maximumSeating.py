def maximum_seating(lst: list[int]):
    count = 0
    for i in range(len(lst)):
        left_bound = i - 2
        if sum(lst[left_bound if left_bound >= 0 else 0:i]) == 0 and sum(lst[i + 1: i + 3]) == 0 and lst[i] != 1:
            count += 1
            lst[i] = 1
    return count


if __name__ == '__main__':
    print(maximum_seating([1, 0, 0, 0, 0, 0, 0, 1]))
