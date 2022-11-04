from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # b - c - d = a
        # a - c - d = b
        # a - b - d = c
        # a - b - c = d
        nums_clone = []
        pairs = []
        i, j, k, l = 0, 0, 0, 0
        while i < len(nums):
            a = abs(nums[i] - target)
            nums_clone = nums[0:i] + nums[i + 1:]
            while j < len(nums_clone):
                b = a - nums_clone[j]
                j += 1
                if b in nums_clone:
                    b_ind = nums_clone.index(b)
                    nums_clone = nums_clone[0:b_ind] + nums_clone[b_ind + 1:]
                    while k < len(nums_clone):
                        c = nums_clone[k] - b
                        k += 1
                        if c in nums_clone:
                            c_ind = nums_clone.index(c)
                            nums_clone = nums_clone[0: c_ind] + nums_clone[c_ind:]
                            while l < len(nums_clone):
                                d = nums_clone[l] - c
                                l += 1
                                if d in nums_clone:
                                    ## found pair
                                    if sorted([a, b, c, d]) not in pairs and a + b + c + d == target:
                                        print(
                                            a, b, c, d, nums_clone)
                                        pairs.append(sorted([a, b, c, d]))
                                        j, k, l = 0, 0, 0
                                        break
                            l = 0
                    k = 0
            j = 0
            i += 1
        return pairs


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum([2,2,2,2,2], 8))