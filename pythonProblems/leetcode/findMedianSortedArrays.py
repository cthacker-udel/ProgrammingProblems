from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)
        return (combined[len(combined) // 2] + combined[(len(combined) // 2) - 1]) / 2 if len(combined) % 2 == 0 else combined[len(combined) // 2]
