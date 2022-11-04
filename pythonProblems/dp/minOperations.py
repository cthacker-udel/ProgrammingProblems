
class Solution:

    def __init__(self):
        self.min_op_hash = {}

    def minOperation(self, n, targ=1, steps=1):
        if targ in self.min_op_hash:
            return self.min_op_hash[targ]
        elif targ > n:
            self.min_op_hash[targ] = steps + 1
            return steps + 1
        elif targ == n:
            self.min_op_hash[targ] = steps
            return steps
        else:
            print(self.min_op_hash)
            return min(self.minOperation(n, targ * 2, steps + 1), self.minOperation(n, targ + 1, steps + 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperation(142421))
