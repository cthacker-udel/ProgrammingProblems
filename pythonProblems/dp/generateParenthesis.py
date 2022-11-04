
from copy import deepcopy
from typing import List


class Solution:
    def generateParenthesis(self, n: int, generated_parens: List[str] = None, open_count=0, close_count=0, curr_pair: str = '') -> List[str]:
        if generated_parens == None:
            generated_parens = []
        if open_count == close_count and open_count + close_count == (n * 2):
            generated_parens.append(curr_pair)
            return generated_parens
        else:
            if close_count > open_count or open_count + close_count > (n * 2):
                return ['']
            self.generateParenthesis(n, generated_parens, open_count, close_count + 1,
                                     curr_pair + ')')
            self.generateParenthesis(n, generated_parens, open_count + 1, close_count,
                                     curr_pair + '(')
        return generated_parens


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(2))
    print(sol.generateParenthesis(1))
