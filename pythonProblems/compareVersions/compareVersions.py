def compare_versions(version1: str, version2: str):
    _ind1 = version1.find('.')
    _ind2 = version2.find('.')
    if _ind1 >= 0 or _ind2 >= 0:
        split_periods_1 = version1.split('.')
        split_periods_2 = version2.split('.')
        for i in range(min(len(split_periods_1), len(split_periods_2))):
            elem_1 = split_periods_1[i]
            elem_2 = split_periods_2[i]
            if int(elem_1) < int(elem_2):
                return False
        return True if len(split_periods_1) == len(split_periods_2) else True if len(split_periods_1) > len(split_periods_2) else False
    else:
        return int(version1) >= int(version2)


if __name__ == '__main__':
    left_values = ['11', '11', '10.4.6', '10.4', '10.4', '10.4.9']
    right_values = ['10', '11', '10.4', '11', '10.10', '10.5']
    for eachpair in zip(left_values, right_values):
        print(compare_versions(eachpair[0], eachpair[1]))
