class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        output = ''
        value_keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        starting_value = 12

        while num > 0:
            val_ = value_keys[starting_value]
            if num >= val_:
                num -= val_
                output += values[value_keys[starting_value]]
            else:
                starting_value -= 1

        return output


if __name__ == '__main__':
    sol = Solution()
    sol.intToRoman(58)
