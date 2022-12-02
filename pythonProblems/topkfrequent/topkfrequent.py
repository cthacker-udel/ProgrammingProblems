from operator import itemgetter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for eachnumber in nums: # O(n)
            if eachnumber in hashmap:
                hashmap[eachnumber] += 1
            else:
                hashmap[eachnumber] = 1
        keys = sorted(list(hashmap.items()), key=itemgetter(1))
        t_keys = keys[len(keys) - k:]
        nums = []
        for eachentry in t_keys:
            nums.append(eachentry[0])
        return nums

    

if __name__ == '__main__':
    elems = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(elems, k))