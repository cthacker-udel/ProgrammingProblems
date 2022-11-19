from typing import List


def find_us(n1: int, n2: int, k: int, prime_factors: List[int], digits: List[int]):
    """
    """
    def generate_permutations(astr: str, permutes: List[str] | None = None, ind: int = 0) -> List[str]:
        """
        """
        if permutes is None:
            permutes = []
        if ind == len(astr):
            return permutes
        for i in range(len(astr)):
            modified_str = list(astr)
            modified_str[i], modified_str[ind] = modified_str[ind], modified_str[i]
            found_permutes = generate_permutations(
                ''.join(modified_str), permutes + [''.join(modified_str)], ind + 1)
            for eachpermute in found_permutes:
                if not eachpermute in permutes:
                    permutes.extend([eachpermute])
        return permutes
    start = n1
    end = n1 + (k * n2)
    end_str = str(end)
    end_str_len = len(end_str)
    numbers = []
    start_digit = end_str[0]
    if len(digits) == end_str_len:
        # digits is number of digits in end, only permute digits to find numerical values
        pass
    else:
        # travel down the possible iterations, counting the # of digits, such as if the end is
        # 300, we go 300, 200, 100. For 5000, we go 5000, 4000, 3000, 2000, 1000, then decrement the # of digits to 3, going
        # 900, 800, 700, and so on. Checking if the digits are within the number
        base_number = ''.join([str(x) for x in digits])
        gathered_perms = []
        starting_number = base_number
        while len(digits) <= end_str_len:
            while len(starting_number) < end_str_len - 1:
                starting_number += '0'
            starting_perms = generate_permutations(
                end_str[0] + starting_number)
            for eachperm in starting_perms:
                intified_perm = int(''.join(eachperm))
                if intified_perm < end and intified_perm > start:
                    gathered_perms.append(intified_perm)
            starting_number = base_number
            end_str_len -= 1
        base_perms = generate_permutations(base_number)
        print(gathered_perms)


if __name__ == '__main__':

    astr = 'hello'
    # 1 2 3 | 1 3 2 | 2 1 3 | 2 3 1 | 3 1 2 | 3 2 1
    print(find_us(30, 400, 18, [2, 3, 7], [6, 2, 5]))

    # n1 = 30
    # n2 = 400
    # k = 18
    # prime_factors = [2, 3, 7]
    # digits = [6, 2, 5]
    # find_us(n1, n2, k, prime_factors, digits)
