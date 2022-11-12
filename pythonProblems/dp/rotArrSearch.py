from typing import List


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l != r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
        return -1


if __name__ == '__main__':
    sol = Solution()
    sol.search([4, 5, 6, 7, 0, 1, 2], 0)