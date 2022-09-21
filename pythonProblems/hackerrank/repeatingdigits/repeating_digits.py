from itertools import permutations


class Solution:

    def permute(n: int, r: int) -> int:
        non_repeating_numbers = 1
        for i in range(0, r):
            non_repeating_numbers *= n
            n -= 1
        return non_repeating_numbers

    def numDupDigitsAtMostN(self, n: int) -> int:
        lst: list = []
        count = 0

        temp = n + 1
        while temp != 0:
            lst.insert(0, temp % 10)
            temp = temp // 10

        for i in range(0, len(lst) - 1):
            count += 9 * Solution.permute(9, i)

        num_set = []
        for i in range(0, len(lst)):
            start_j = 1 if i == 0 else 0
            print(lst)
            for j in range(start_j, lst[i]):
                if num_set.count(j):
                    continue
                else:
                    count += Solution.permute(10 - (i + 1), len(lst) - 1 - i)
            if num_set.count(lst[i]):
                break
            num_set.append(lst[i])
        return n - count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDupDigitsAtMostN(1000))
