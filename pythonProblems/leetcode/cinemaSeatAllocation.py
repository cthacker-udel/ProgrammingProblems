from operator import itemgetter
from typing import List


class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = {}
        for seat in reservedSeats:
            if seat[0] in seats:
                seats[seat[0]].append(seat[1])
            else:
                seats[seat[0]] = [seat[1]]
        families = abs(len(seats.keys()) - n) * 2
        for i in seats:
            taken = seats[i]
            if len(taken) == 2 and 1 in taken and 10 in taken:
                families += 2
            elif 1 in taken and max(taken) == 1:
                families += 2
            elif 10 in taken and min(taken) == 10:
                families += 2
            elif 2 not in taken and 3 not in taken and 4 not in taken and 5 not in taken:
                families += 1
            elif 4 not in taken and 5 not in taken and 6 not in taken and 7 not in taken:
                families += 1
            elif 6 not in taken and 7 not in taken and 8 not in taken and 9 not in taken:
                families += 1
        return families


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxNumberOfFamilies(
        4,
        [[4, 3], [1, 4], [4, 6], [1, 7]]
    ))
