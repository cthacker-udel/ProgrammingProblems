from typing import List
import itertools

combos = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}


def generate_perms(k, arr):
    if k == 1:
        print(arr)
        return arr
    else:
        generate_perms(k - 1, arr)

        for i in range(k):
            generate_perms(k - 1, arr)

            if k % 2 != 0:
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            else:
                arr[i], arr[k - 1] = arr[k - 1], arr[i]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        representations = ["0", "1", "abc", "def",
                           "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = []
        if len(digits) == 0:
            return queue
        queue.append("")

        for i in range(len(digits)):
            ind = int(digits[i])
            while len(queue[0]) == i:
                permutation = queue[0]
                del queue[0]
                for eachchar in representations[ind]:
                    queue.append(permutation + eachchar)
        return queue


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))
