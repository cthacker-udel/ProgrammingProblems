from typing import List, Union

# e = a + b + c + d
# a = b + c + d
# b = a + c + d


## target = 4
## 4 - 1 == 3, so check for pairs for 1 and 3, if both have pairs then we have a four-sum
## 4 + (-1 + 2) + (2 + 1) == 4 + (1) + (3) == 4


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        pairs = []
        for ind, elem in enumerate(sorted_nums):
            for ind2, elem2 in enumerate(sorted_nums):
                if ind2 != ind:
                    ## l, r sol
                    l = 0
                    r = len(sorted_nums) - 1
                    ## summing to second number
                    the_sum = sorted_nums[l] + sorted_nums[r]
                    while l != r:
                        if the_sum < elem2:
                            l += 1
                        elif the_sum > elem2:
                            r += 1
                        elif the_sum == elem2:
                            pairs.append([elem, elem2])

                        

        


if __name__ == '__main__':
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    sol = Solution()
    sol.fourSum(nums, target)
