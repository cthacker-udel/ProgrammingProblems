from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_num = nums[0] + nums[1] + nums[2]
        for i in range(num_len - 2):
            l_ = i + 1
            r_ = num_len - 1
            while l_ < r_:
                res = nums[i] + nums[l_] + nums[r_]
                if res == target:
                    return res

                if abs(target - res) < abs(closest_num - target):
                    closest_num = res

                if res > target:
                    r_ -= 1
                else:
                    l_ += 1
        return closest_num


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest([0, 1, 2],
                              3
                              ))
