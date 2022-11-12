from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 0:
            return [-1, -1]
        if (nums[0], nums[-1]) == (target, target):
            return [0, nums_len - 1]
        mid = nums_len // 2
        l = 0
        r = nums_len - 1
        while nums[mid] != target and l < r:
            if nums[mid] > target:
                ##left side
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            mid = l + ((r - l) // 2)
        if nums[mid] == target:
            ## search left, and right
            left_pt = mid
            right_pt = mid
            while (left_pt >= 0 and nums[left_pt] == target) or (right_pt < nums_len and nums[right_pt] == target):
                if left_pt >= 0:
                    if nums[left_pt] == target:
                        left_pt -= 1
                if right_pt < len(nums):
                    if nums[right_pt] == target:
                        right_pt += 1
            return [left_pt + 1, right_pt - 1]
        return [-1, -1]


if __name__ == '__main__':
    arr = [0,0,1,2,2]
    target = 0
    sol = Solution()
    print(sol.searchRange(arr, target))