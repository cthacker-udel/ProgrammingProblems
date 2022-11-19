
from typing import List


def solve_stones(num_piles: int, stone_piles: List[int]) -> str:
    if num_piles % 2 != 0 and num_piles > 0:  # is number of stone piles odd
        return "Mike"
    if stone_piles == 0:
        return "Joe"
    min_elem = min(stone_piles)
    if stone_piles.index(min_elem) % 2 != 0:  # if it's odd, Mike loses
        return "Mike"
    else:
        return "Joe"


if __name__ == '__main__':
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        num_piles, piles = int(input()), [int(x) for x in input().split(" ")]
        print(solve_stones(num_piles, piles))
