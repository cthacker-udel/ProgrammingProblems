from typing import List

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    elif num == 2 or num == 3 or num == 5:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    else:
        for i in range(2, int(num**.5) + 1):
            if num % i == 0:
                return False
        return True

def prime_factorize(num: int) -> List[int]:
    num = abs(num)
    if is_prime(num):
        return [num]
    else:
        starter_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        start_len = 25
        start_ind = 0
        factors = set()
        while start_ind < start_len and num > 1:
            if num % starter_list[start_ind] == 0:
                ## found factor
                while num % starter_list[start_ind] == 0:
                    factors.add(starter_list[start_ind])
                    num //= starter_list[start_ind]
                if is_prime(num):
                    factors.add(num)
                    break
                start_ind = 0
                continue
            start_ind += 1
        if num > 1:
            for i in range(2, int(num**.5) * int(num **.75)):
                if num % i == 0 and is_prime(i):
                    factors.add(i)
                    while num % i == 0:
                        num //= i
        return list(factors)



def sum_for_list(lst: List[int]):
    prime_sums = {}
    for eachnum in lst:
        prime_factors = prime_factorize(eachnum)
        for each_factor in prime_factors:
            if each_factor in prime_sums:
                prime_sums[each_factor] += eachnum
            else:
                prime_sums[each_factor] = eachnum
    answer = []
    for eachkey in sorted(prime_sums.keys()):
        answer.append([eachkey, prime_sums[eachkey]])
    return answer


if __name__ == '__main__':
    a = [15, 30, -45]
    print(sum_for_list(a))
    print('list2')
    a = [15, 21, 24, 30, 45]
    print(sum_for_list(a))
    print('list3')
    a = [12, 15]
    print(sum_for_list(a))
    print('list4')
    a = [-29804, -4209, -28265, -72769, -31744]
    print(sum_for_list(a))
    a = [981650, -292104, -57569, -500682, -901430, 694257, -453700, -185313]
    print('list5')
    print(sum_for_list(a))
    # [
    #   [2, -1166266], [3, -283842], [5, -373480], [7, -500682], 
    #   [13, -954382], [23, -57569], [29, 981650], 
    #   [109, -901430], [131, -500682], [223, -185313], [277, -185313], 
    #   [349, -453700], [677, 981650], [827, -901430], [2503, -57569], 
    #   [4057, -292104], [231419, 694257]]