class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sums = []
        stack = []
        count = 0
        for ind, eachparen in enumerate(s):
            if eachparen == '(':
                stack.append('(')
                count += 1
                if ind < len(s) - 1 and len(stack) > 1 and len(s[ind + 1:]) < len(stack):
                    print('in if', ind)
                    sums.append(0)
                    sums.append(count - len(stack))
                    sums.append(0)
                    stack = []
                    count = 0
            elif eachparen == ')':
                if len(stack) == 1:
                    stack.pop()
                    sums.append(count + 1)
                    count = 0
                elif len(stack) > 0:
                    stack.pop()
                    count += 1
                else:
                    sums.append(0)
        if len(stack) > 0:
            sums.append(0)
            sums.append(count - len(stack))
        print(sums)
        running_total = 0
        running_sums = []
        for eachnum in sums:
            if eachnum == 0:
                running_sums.append(running_total)
                running_total = 0
            else:
                running_total += eachnum
        running_sums.append(running_total)
        return max(running_sums) if len(running_sums) > 0 else 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses("(()")) # 4
