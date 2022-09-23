class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '.' not in p and '*' not in p:
            if len(s) == len(p):
                return s == p
            return False
        i = 0
        j = 0
        while j < len(p) - 1 and i < len(s):
            if p[j + 1] == '*':
                ## two decisions, whether to use or not to use
                if s.count(p[j]) == 0 and p[j] != '.':
                    ## choose not to use
                    j += 2
                    continue
                elif p[j] == s[i] or p[j] == '.':
                    for k in range(i, len(s)):
                        if s[k] == p[j] or p[j] == '.':
                            i += 1
                        else:
                            break
                    j += 2

            elif p[j] == '.':
                j += 1
            else:
                if p[j] != s[i]:
                    return False
                else:
                    j += 1
                    i += 1
        return p[j] == s[i] or p[j] == '.' if j < len(p) else True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch("mississippi"
                      "mis*is*p*."
                      ))
