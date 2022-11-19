from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int, combos: List[List[int]] = None, curr_combo_sum: int = None, curr_combo: List[int] = None, curr_combo_indices: List[int] = None) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        if combos is None:
            combos = []
        if curr_combo is None:
            curr_combo = []
        if curr_combo_indices is None:
            curr_combo_indices = []
        
        curr_combo_sum = 0
        if not combos is None:
            curr_combo_sum = sum(curr_combo)
        
        for ind, elem in enumerate(candidates):
            if elem + curr_combo_sum > target:
                continue
            if elem + curr_combo_sum == target and ind not in curr_combo_indices:
                combo_sorted = sorted(curr_combo + [elem])
                if combo_sorted not in combos:
                    combos.append(combo_sorted)
            elif ind not in curr_combo_indices: 
                acquired_combos = self.combinationSum2(candidates, target, combos, curr_combo_sum, curr_combo + [elem], curr_combo_indices + [ind])
                for eachcombo in acquired_combos:
                    eachcombo_sorted = sorted(eachcombo)
                    if eachcombo_sorted not in combos:
                        combos.append(eachcombo_sorted)
        return combos

if __name__ == '__main__':
    sol = Solution()
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 30
    print(sol.combinationSum2(candidates, target))
            