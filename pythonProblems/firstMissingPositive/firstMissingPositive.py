from typing import List


class Solution:
    def countingSort(self, arr, exp1):
        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = arr[i] / exp1
            count[int((index) % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] / exp1
            output[count[int((index) % 10)] - 1] = arr[i]
            count[int((index) % 10)] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    # Method to do Radix Sort
    def radixSort(self, arr, max1):

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
            self.countingSort(arr, exp)
            exp *= 10
        return arr

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Find the first missing positive number in O(n) time, meaning that we cycle through the array once and only once, no double fors

        Args:
            nums (List[int]): list of numbers to analyze

        Returns:
            int: the first missing positive
        """
        altered_nums = set()
        the_sum = 0
        for each_number in nums:
            if each_number > 0 and each_number not in altered_nums:
                altered_nums.add(each_number)
                the_sum += each_number

        arr = self.radixSort(list(altered_nums), max(altered_nums))

        print(arr)

        if len(arr) == 0:
            return 1

        min_number = arr[0]
        max_number = arr[-1]
        range_sum = ((min_number + max_number) * (max_number - min_number + 1)) // 2
        if range_sum == the_sum and min_number == 1:
            return max_number + 1
        else:
            if min_number == 1:
                ## cycle through, find gap, return
                for i in range(len(arr) - 1):
                    if arr[i + 1] - arr[i] > 1:
                        return arr[i] + 1
                return -1
            return 1

    def firstMissingPositiveV2(self, nums: List[int]) -> int:

        n = len(nums)
        r_n = range(n)
        for i in r_n:
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in r_n:
            i_abs = abs(nums[i])

            if i_abs > n:
                continue

            i_abs -= 1
            if nums[i_abs] > 0:
                nums[i_abs] = -1 * nums[i_abs]

        for i in r_n:
            if nums[i] >= 0:
                return i + 1

        return n + 1


if __name__ == "__main__":
    a = [1, 2, 0]
    b = [3, 4, -1, 1]
    c = [7, 8, 9, 11, 12]
    d = [2]
    e = [1, 1]
    f = [
        3,
        17,
        7,
        16,
        16,
        8,
        -4,
        5,
        -4,
        3,
        -2,
        18,
        34,
        5,
        1,
        -7,
        3,
        3,
        27,
        8,
        23,
        3,
        -3,
        2,
        27,
        8,
        15,
        7,
        -6,
        15,
        23,
        -6,
        3,
        2,
        5,
        23,
        21,
        3,
        2,
    ]
    sol = Solution()
    print(sol.firstMissingPositiveV2(a))
    print(sol.firstMissingPositiveV2(b))
    print(sol.firstMissingPositiveV2(c))
    print(sol.firstMissingPositiveV2(d))
    print(sol.firstMissingPositiveV2(e))
    print(sol.firstMissingPositiveV2(f))
