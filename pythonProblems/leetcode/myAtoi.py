import string


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        constructed_dig: str = ''
        signStr = '+-'
        max_dig = 2147483648
        signs = []
        for eachchar in s:
            if eachchar == ' ':
                break
            else:
                if eachchar in signStr:
                    if len(signs) > 0:
                        break
                    elif len(constructed_dig) > 0:
                        break
                    signs.append(eachchar)
                elif eachchar.isdigit():
                    constructed_dig += eachchar
                else:
                    break
        if len(constructed_dig) == 0 or len(signs) > 1:
            return 0
        else:
            atoid = int(constructed_dig)
            if atoid >= max_dig:
                return (max_dig - 1) if ((len(signs) > 0 and signs[0] == '+') or len(signs) == 0) else -1 * max_dig
            else:
                return atoid if ((len(signs) > 0 and signs[0] == '+') or len(signs) == 0) else -1 * atoid


if __name__ == '__main__':
    sol = Solution()
    sol.myAtoi("-5-")
