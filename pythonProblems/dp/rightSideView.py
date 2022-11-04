from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    levels = []

    def rightSideView(self, root: Optional[TreeNode], level=0) -> List[int]:
        if root == None:
            return []
        else:
            if level in Solution.levels:
                return []
            result = [root.val] + Solution.rightSideView(
                self, root.right, level + 1) + Solution.rightSideView(self, root.left, level + 1)
            Solution.levels.append(len(Solution.levels))
            return result


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1, None, TreeNode(3))
    print(sol.rightSideView(root))
