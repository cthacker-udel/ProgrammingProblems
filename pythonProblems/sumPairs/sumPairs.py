from typing import List, Dict

def sum_pairs(ints: List[int], s: int):
    lowest_index = float('inf')
    top_pair = []
    nums_dict: Dict[int, List[int]] = {}
    for i, elem in enumerate(ints):
        if elem in nums_dict:
            nums_dict[elem].append(i)
        else:
            nums_dict[elem] = [i]
    for eachkey in nums_dict:
        if s - eachkey in nums_dict: ## check if pair exists
            lowest_ind_eachkey = nums_dict[eachkey][0]
            lowest_ind_sminus = nums_dict[s - eachkey][0]
            if lowest_ind_eachkey < lowest_ind_sminus and lowest_ind_sminus < lowest_index:
                lowest_index = lowest_ind_sminus
                top_pair = [eachkey, s - eachkey]
            elif lowest_ind_sminus < lowest_ind_eachkey and lowest_ind_eachkey < lowest_index:
                lowest_index = lowest_ind_eachkey
                top_pair = [s - eachkey, eachkey]
            elif lowest_ind_eachkey == lowest_ind_sminus and len(nums_dict[eachkey]) > 1 and nums_dict[eachkey][1] < lowest_index:
                lowest_index = nums_dict[eachkey][1]
                top_pair = [eachkey, eachkey]
    return None if not top_pair else top_pair

def sum_pairs_v2(ints: List[int], s: int) -> List[int]:
    i = 0
    j = len(ints) - 1
    nums_dict: Dict[int, List[int]] = {}
    for ind, elem in enumerate(ints):
        if elem in nums_dict:
            nums_dict[elem].append(ind)
        else:
            nums_dict[elem] = [ind]
    ints.sort() # O(n lg n)
    lowest_ind = float('inf')
    top_pair = []
    while i < j:
        _sum = ints[i] + ints[j]
        if _sum == s and j < lowest_ind and nums_dict[ints[i]][0] < nums_dict[ints[j]][0] and nums_dict[ints[j]][0] < lowest_ind:
            top_pair = [ints[i], ints[j]]
            lowest_ind = nums_dict[ints[j]][0]
            j -= 1
        elif _sum > s:
            j -= 1
        else:
            i += 1
    print(top_pair)



if __name__ == '__main__':
    l1 = [1, 4, 8, 7, 3, 15]
    l2 = [1, -2, 3, 0, -6, 1]
    l3 = [20, -13, 40]
    l4 = [1, 2, 3, 4, 1, 0]
    l5 = [10, 5, 2, 3, 7, 5]
    l6 = [4, -2, 3, 3, 4]
    l7 = [0, 2, 0]
    l8 = [5, 9, 13, -3]
    l9 = [1] * 10000000
    l9[len(l9) // 2 - 1] = 6
    l9[len(l9) // 2] = 7
    l9[len(l9) - 2] = 8
    l9[len(l9) - 1] = -3
    l9[0] = 13
    l9[1] = 3

    print(sum_pairs(l1, 8) == [1, 7])# "Basic: %s should return [1, 7] for sum = 8" % l1)
    print(sum_pairs(l2, -6) == [0, -6])# "Negatives: %s should return [0, -6] for sum = -6" % l2)
    print(sum_pairs(l3, -7) is None)# "No Match: %s should return None for sum = -7" % l3)
    print(sum_pairs(l4, 2) == [1, 1])# "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
    print(sum_pairs(l5, 10) == [3, 7])# "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
    print(sum_pairs(l6, 8) == [4, 4])# "Duplicates: %s should return [4, 4] for sum = 8" % l6)
    print(sum_pairs(l7, 0) == [0, 0])# "Zeroes: %s should return [0, 0] for sum = 0" % l7)
    print(sum_pairs(l8, 10) == [13, -3])# "Subtraction: %s should return [13, -3] for sum = 10" % l8)
    print(sum_pairs(l9, 13) == [6, 7])# "Ten Million Numbers With Middle Pair: Should terminate with a valid pair output")
    print(sum_pairs(l9, 5) == [8, -3])# "Ten Million Numbers With Pair At End: Should terminate with a valid pair output")
    print(sum_pairs(l9, 16) == [13, 3])# "Ten Million Numbers With Pair At Start: Should terminate with a valid pair output")
    print(sum_pairs(l9, 31) is None)# "Ten Million Numbers With No Match: Should return None in a decent time period")