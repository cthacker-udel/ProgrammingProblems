class Solution:
    def reverse(self, x: int) -> int:
        res = -1 * int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        return res if res <= 2147483648 and res >= -2147483648 else 0


if __name__ == '__main__':
    sol = Solution()
