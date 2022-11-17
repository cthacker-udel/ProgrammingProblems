import random
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_number = -1
        max_number = 0
        gap_base = -1
        for eachnum in nums:
            if eachnum > 0:
                if min_number == -1:
                    ## initialize all trackers
                    max_number = eachnum
                    min_number = eachnum
                else:
                    gap = abs(eachnum - max_number)
                    gap_base_diff = abs(eachnum - gap_base)
                    if gap > 1 and ((eachnum > max_number and gap_base == -1) or (eachnum < max_number and gap_base == -1) or (eachnum < max_number and gap_base_diff == 1) or (eachnum < max_number and gap_base_diff > 0 and eachnum < gap_base)): ## before and after
                        if gap_base_diff == 1:
                            gap_base = eachnum
                        elif gap_base == -1:
                            gap_base = min(max_number, eachnum)
                        else:
                            gap_base = min(max_number, eachnum)
                    min_number = min(min_number, eachnum)
                    max_number = max(max_number, eachnum)
        if min_number != 0 and min_number > 1:
            return 1
        if gap_base == -1:
            ## no gaps detected, check max, if max is 0, return 1
            if max_number == 0:
                return 1
            # return max + 1
            return max_number + 1
        else:
            return gap_base + 1



if __name__ == '__main__':
    sol = Solution()
    arrs = [
        [1,2,0],
        [3,4,-1,1],
        [7,8,9,11,12],
        [1, 2, 3, 50, 48, 5214, 32, 6324, 234, -32, -1231, -432134, -5123, -412243, -44, -324, 0],
        [1, 2, 3, 6, 7, 4],
        [40, 33, 50, -11, 0, 12, 50, 1, 33, -1, -3, 27, 29, -19],
        [1,2,6,3,5,4]
    ]
    # for i in range(5):
    #     new_arr = []
    #     for j in range(random.randint(10, 30)):
    #         new_arr.append(random.randint(-20, 50))
    #     arrs.append(new_arr)
    #     new_arr = []
    for eacharr in arrs:
        print('testing {}'.format(eacharr))
        print(sol.firstMissingPositive(eacharr))