from typing import List


def generate_determinant(matrix: List[List[int]], column_index: int) -> List[List[int]]:
    """
    Generates the determinant from the column index given, which means that the column is removed alongside the row in which the element is present

    Args:
        matrix (List[List[int]]): The matrix given
        column_index (int): The index of the column to remove

    Returns:
        List[List[int]]: The matrix modified to have the determinant applied
    """
    cloned_matrix: List[List[int]] = [x[:] for x in matrix]
    i = 0
    del cloned_matrix[i]
    for each_row in cloned_matrix:
        del cloned_matrix[i][column_index]
        i += 1
    return cloned_matrix


def determinant(matrix: List[List[int]]) -> int:
    """
    Generates a determinant of the matrix passed into the function

    Args:
        matrix (List[List[int]]): The matrix we are given to calculate the determinant of

    Returns:
        int: The determinant of the matrix, as described above.
    """
    ## what we have to do, is to first have 2 cases: 1x1, and 2x2, then we just basically do this
    # for each part of the matrix, we generate the determinant of the first row, by passing in the generated matrix into this same function, which will eventually
    # return a value for whichever matrix we pass into it
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant_sum = 0
        minus_ = False
        # generate determinant of first row
        for j in range(len(matrix[0])):
            if minus_:
                determinant_sum -= matrix[0][j] * determinant(
                    generate_determinant(matrix, j)
                )
            else:
                determinant_sum += matrix[0][j] * determinant(
                    generate_determinant(matrix, j)
                )
            minus_ = not minus_
        return determinant_sum


if __name__ == "__main__":
    m1 = [[4, 6], [3, 8]]
    m5 = [[2, 4, 2], [3, 1, 1], [1, 2, 0]]
    m6 = [
        [
            2,
        ]
    ]
    print(determinant([[5]]))
    print(determinant(m5))

    """
    | 2 4 2 |
    | 3 1 1 |
    | 1 2 0 |
    """
