from typing import List, Union

# e = a + b + c + d
# a = b + c + d
# b = a + c + d


## target = 4
## 4 - 1 == 3, so check for pairs for 1 and 3, if both have pairs then we have a four-sum
## 4 + (-1 + 2) + (2 + 1) == 4 + (1) + (3) == 4


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pairs = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    elem_i = nums[i]
                    elem_j = nums[j]
                    elem_k = nums[k]
                    diff = target - (elem_i + elem_j + elem_k)
                    if i != j and j != k and k != i:
                        altered_arr = nums[:]
                        indexes = sorted([i, j, k])
                        del altered_arr[indexes[2]]
                        del altered_arr[indexes[1]]
                        del altered_arr[indexes[0]]
                        if diff in altered_arr:
                            sorted_pair = sorted(
                                [diff, elem_i, elem_j, elem_k])
                            if sorted_pair not in pairs:
                                pairs.append(sorted_pair)
        return pairs


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 2]
    target = 8
    sol = Solution()
    print(sol.fourSum(nums, target))

    # def threeSum(self, nums: List[int], target: int) -> Union[List[int], None]:
    #     for i in range(len(nums)):
    #         result = target - nums[i]
    #         if result in nums:
    #             j = nums.index(result)
    #             result = Solution.twoSum(self, nums[:j] + nums[j + 1:], result)
    #             return [target] + result if result != None else []
    #     return None
