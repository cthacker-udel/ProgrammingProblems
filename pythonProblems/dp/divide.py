import math


class Solution:
    neg_lim = -2147483648
    pos_lim = 2147483648 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        elif divisor == -1:
            if dividend < 0:
                ## flips to positive, account for case
                return abs(dividend) if abs(dividend) < Solution.pos_lim else Solution.pos_lim
            else:
                return -1 * dividend
        dividend = dividend if dividend >= Solution.neg_lim and dividend <= Solution.pos_lim else Solution.neg_lim if dividend < 0 else Solution.pos_lim
        is_negative = (dividend < 0 and divisor > 0) or (
            divisor < 0 and dividend > 0)
        res = math.exp(math.log(abs(dividend)) -
                       math.log(abs(divisor))) + 0.0000000001
        return int(res) if not is_negative else -1 * int(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.divide(-231, 3))
