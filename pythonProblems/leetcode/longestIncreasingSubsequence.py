from typing import List

## problem 2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        n = len(nums) - 1
        dp[n] = 1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[i] = max(dp[i], 1 + dp[j] if nums[i] < nums[j] else 0)
        return max(dp)


if __name__ == '__main__':
    l = Solution()
    print(l.lengthOfLIS([7,7,7,7,7,7,7]))
    
