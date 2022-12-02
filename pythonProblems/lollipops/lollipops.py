import math

def santa():
    num_tests = int(input())
    for i in range(num_tests):
        the_str = input()
        distinct_letters = []
        days = 0
        for eachchar in the_str:
            if eachchar not in distinct_letters and len(distinct_letters) == 3:
                days += 1
                distinct_letters = [eachchar]
            elif eachchar in distinct_letters:
                continue
            else:
                distinct_letters.append(eachchar)
        print(days + 1)


if __name__ == '__main__':
    santa()