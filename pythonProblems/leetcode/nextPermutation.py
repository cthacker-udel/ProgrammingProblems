from typing import List


class Solution:

    def find_successor(self, nums: List[int], val: int) -> int:
        sorted_nums = sorted([x for x in set(nums + [val])])
        ind_ = sorted_nums.index(val)
        if ind_ == len(sorted_nums) - 1:
            ## no successor, return -1
            return -1
        return sorted_nums[ind_ + 1]

    def nextPermutation(self, nums: List[int]) -> None:
        print('arr = ', nums)
        if sorted(nums)[::-1] == nums:
            ## return to default
            nums[:] = sorted(nums)
        else:
            for i in range(1, len(nums)):
                sorted_section = sorted(nums[i:])[::-1]
                if sorted_section == nums[i:]:
                    ## swap second max with one before, find successor of previous index and replace
                    successor = Solution.find_successor(self, sorted_section, nums[i - 1])
                    successor_ind = sorted_section.index(successor)
                    nums[i - 1], nums[i:] = successor, sorted(sorted_section[:successor_ind] + [nums[i - 1]] + sorted_section[successor_ind + 1:])
                    return None
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] > nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    return None


if __name__ == '__main__':
    arr = [1, 3, 2]
    arr2 = [1,2,3, 4, 5]
    arr3 = [1,1,5]
    arr4 = [3,2,1]
    arr5 = [1, 2]
    arr6 = [2,3,1]
    arr7 = [5,4,7,5,3,2]
    arr8 = [2,2,7,5,4,3,2,2,1]
    arr9 = [1,5,1]
    sol = Solution()
    for eacharr in [arr, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]:
        sol.nextPermutation(eacharr)
    for eacharr in [arr, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]:
        print(eacharr)