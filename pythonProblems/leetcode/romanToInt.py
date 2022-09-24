class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        doubles = ["IV", "IX", "XL", "XC", "CD", "CM"]

        total = 0
        i = 0
        while i < len(s):
            first_ = s[i]
            second_ = s[i + 1] if i < len(s) - 1 else ''
            if f'{first_}{second_}' in doubles:
                total += values[f'{first_}{second_}']
                i += 2 if i < len(s) - 1 else 1
            else:
                total += values[f'{first_}']
                i += 1
        return total


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("LVIII"))
