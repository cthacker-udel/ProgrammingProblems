from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total: float = 0
        running_decrease: int = 0
        brackets_clone = [x[:] for x in brackets]
        for i, each_bracket in enumerate(brackets):
            if running_decrease != 0:
                each_bracket[0] -= running_decrease
            left_ = each_bracket[0] - income
            if left_ <= 0:
                # income is > each_bracket[0]
                total += each_bracket[0] * (each_bracket[1] / 100)
                income -= each_bracket[0]
            else:
                total += income * (each_bracket[1] / 100)
                income = 0
            running_decrease = brackets_clone[i][0]
        return total


if __name__ == "__main__":
    a = [[3, 50], [7, 10], [12, 25]]
    sol = Solution()
    print(sol.calculateTax(a, 10))
    b = [[1, 0], [4, 25], [5, 50]]
    sol = Solution()
    print(sol.calculateTax(b, 2))
