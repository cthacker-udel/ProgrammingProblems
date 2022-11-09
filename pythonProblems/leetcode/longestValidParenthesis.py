class Solution:
    def longestValidParentheses(self, paren: str) -> int:
        stack = []
        longest = 0
        curr_len = 0
        for elem in paren:
            if elem == '(':
                stack.append('(')
            elif elem == ')':
                if len(stack) == 0:
                    longest = max(curr_len, longest)
                    curr_len = 0
                else:
                    stack.pop()
                    curr_len += 2
                    if len(stack) == 0:
                        longest = max(longest, curr_len)
                        curr_len = 0
        longest = max(longest, curr_len)
        return longest

            
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses(")()())"))