from typing import List


def find_uniq(arr: List[str]) -> str:
    """
    Given an array of strings, return the one string among all of them that contains similar letters

    Args:
        arr (List[str]): The list of strings we are generating the unique string from

    Returns:
        str: The unique string that does not contain any similar letters among all of the other elements
    """
    unique_strings = {}
    modified_arr = ["".join(sorted(set(x.lower().replace(" ", "")))) for x in arr]

    for ind, element in enumerate(modified_arr):
        if element in unique_strings:
            unique_strings[element] = -1
        else:
            unique_strings[element] = ind
    for ind, element in enumerate(unique_strings.items()):
        if element[1] != -1:
            return arr[element[1]]


if __name__ == "__main__":
    arr2 = ["Aa", "aaa", "aaaaa", "BbBb", "Aaaa", "AaAaAa", "a"]
    arr3 = ["abc", "acb", "bac", "foo", "bca", "cab", "cba"]
    arr = ["    ", "a", "  "]
    arr4 = ["Tom Marvolo Riddle", "I am Lord Voldemort", "Harry Potter"]
    arr5 = ["i", "t", "t", "t"]
    print(find_uniq(arr))
    print(find_uniq(arr2))
    print(find_uniq(arr3))
    print(find_uniq(arr4))
    print(find_uniq(arr5))
