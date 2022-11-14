from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        combos = self.find_combos(sorted_candidates, target)
        filtered_combos = []
        for eachcombo in combos:
            if sorted(eachcombo) in filtered_combos:
                continue
            else:
                filtered_combos.append(sorted(eachcombo))
        print(filtered_combos)
        return filtered_combos
    
    def find_combos(self, nums: List[int], target: int, curr_total_arr: List[int] = None, combos: List[List[int]] = None) -> List[List[int]]:
        curr_total = 0
        if curr_total_arr is None:
            curr_total_arr = []
        else:
            curr_total = sum(curr_total_arr)
        if combos is None:
            combos = []
        for eachnum in nums:
            if eachnum + curr_total < target:
                acquired_combos = self.find_combos(nums, target, curr_total_arr + [eachnum], combos)
                for eachcombo in acquired_combos:
                    if eachcombo not in combos:
                        combos.append(eachcombo)
            elif eachnum + curr_total > target:
                return [] + combos
            else:
                if sorted(curr_total_arr + [eachnum]) not in combos and curr_total + eachnum == target:
                    return combos + sorted([curr_total_arr + [eachnum]])
                return []
        return combos

if __name__ == '__main__':
    candidates = [36,21,2,3,23,24,38,22,11,14,15,25,32,19,35,26,31,13,34,29,12,37,17,20,39,30,40,28,27,33]
    target = 35
    sol = Solution()
    sol.combinationSum(candidates, target)
