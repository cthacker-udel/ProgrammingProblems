from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        num_len = len(nums)
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            b = i + 1
            c = num_len - 1
            while b < c:
                the_sum = a + nums[b] + nums[c]
                if the_sum > 0:
                    c -= 1
                elif the_sum < 0:
                    b += 1
                else:
                    triplets.append([a, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
        return triplets


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]
                       ))
