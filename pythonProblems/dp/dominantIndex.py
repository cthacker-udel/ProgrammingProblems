from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] >= (nums[-2] * 2)
