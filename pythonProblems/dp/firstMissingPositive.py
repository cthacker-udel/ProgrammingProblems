from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_number = -1
        max_number = -1
        if 1 not in nums:
            return 1
        for eachnumber in nums:
            if eachnumber < 0:
                continue
            else:
                min_number = eachnumber if min_number == -1 else min(min_number, eachnumber)
                max_number = eachnumber if max_number == -1 else max(max_number, eachnumber)
        return max_number + 1 if min_number <= 1 else min_number - 1


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 4, -1, 1]
    print(sol.firstMissingPositive(nums))