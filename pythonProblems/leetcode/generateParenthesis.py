from typing import List

class Solution:
    def __init__(self):
        self.pairs = []

    def generateParenthesis(self, n: int) -> List[str]:
        def generate_sub_pair(accumulator: str = '', open_count: int = 0, closed_count: int = 0) -> List[str]:
            if closed_count > open_count:
                return ['']
            if open_count == n and closed_count == n:
                return [accumulator]
            if (open_count + closed_count) > (n * 2):
                return ['']
            return generate_sub_pair(accumulator + '(', open_count + 1, closed_count) + generate_sub_pair(accumulator + ')', open_count, closed_count + 1)
        return [x for x in generate_sub_pair() if x != '']


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))