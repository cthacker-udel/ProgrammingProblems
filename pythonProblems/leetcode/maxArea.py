from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left_ = 0
        right_ = len(height) - 1
        max_water = 0

        while left_ != right_:
            max_water = max(
                (right_ - left_) * min(height[left_], height[right_]), max_water)
            if height[left_] < height[right_]:
                left_ += 1
            elif height[right_] < height[left_]:
                right_ -= 1
            else:
                left_ += 1
        return max_water


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
