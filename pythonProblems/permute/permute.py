from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[int] = []
        self.dfs(nums, len(nums), permutations)
        return permutations

    def dfs(
        self,
        nums: List[int],
        permute_length: int,
        permutations: List[List[int]],
        current_permutation: List[int] = [],
    ) -> None:
        for index, each_number in enumerate(nums):
            # Choice
            new_permutation = current_permutation[:] + [each_number]
            self.dfs(
                nums[:index] + nums[index + 1 :],
                permute_length,
                permutations,
                new_permutation,
            )
        if (
            len(current_permutation) == permute_length
            and current_permutation not in permutations
        ):
            permutations.append(current_permutation)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))
