from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                return mid
            mid = l + ((r - l) // 2)
        if l == -1 or r == -1:
            return 0
        return mid + 1 if nums[mid] < target else mid


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 0
    print(sol.searchInsert(nums, target))