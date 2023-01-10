from typing import List
from sys import maxsize


def remove_smallest(numbers: List[int]) -> List[int]:
    """
    Removes the smallest number from the array, with the lowest index

    Args:
        numbers (List[int]): The array we are removing the smallest number from

    Returns:
        List[int]: The modified list, not a mutation of the array that is passed in
    """
    min_number = maxsize
    min_index = len(numbers) + 1
    cloned_numbers = numbers[:]
    for ind, element in enumerate(cloned_numbers):
        if element < min_number:
            min_number = element
            min_index = ind
    if min_index != len(numbers) + 1:
        del cloned_numbers[min_index]
    return cloned_numbers


if __name__ == "__main__":
    arr = [5, 3, 2, 1, 4]
    print(remove_smallest(arr))
