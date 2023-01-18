from typing import List
import numpy as np


def rotate_transform(lst: List[List[int]], num: int) -> List[List[int]]:
    """
    Rotates a 2d matrix `num` times

    Args:
        lst (List[List[int]]): The 2d matrix
        num (int): The # of times to rotate the matrix

    Returns:
        List[List[int]]: The rotated matrix
    """
    np_arr = np.array(lst)
    np_arr = np.rot90(np_arr, num * -1)
    return np_arr.tolist()


if __name__ == "__main__":
    times = 1
    array = [[2, 4], [0, 0]]
    print(rotate_transform(array, times))
