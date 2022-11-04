from typing import List


class Solution:

    dp = []

    def rob(self, nums: List[int]) -> int:
        Solution.dp = [-1] * (len(nums) + 1)
        result = Solution.initiate_rob(self, nums, len(nums) - 1)
        return result

    def initiate_rob(self, nums: List[int], index: int) -> int:
        if index < 0:
            return 0
        elif Solution.dp[index] >= 0:
            return Solution.dp[index]
        else:
            result = max(Solution.initiate_rob(self, nums, index - 2) +
                         nums[index], Solution.initiate_rob(self, nums, index - 1))
            Solution.dp[index] = result
            return result


if __name__ == '__main__':
    arr = [6, 6, 4, 8, 4, 3, 3, 10]
    sol = Solution()
    print(sol.rob(arr))
