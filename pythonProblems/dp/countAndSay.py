
class Solution:

    def gen_number(self, num: str) -> str:
        sequence_count = {}
        curr_key = ''
        generated_string = ''
        for eachdigit in num:
            if eachdigit in sequence_count:
                sequence_count[eachdigit] += 1
            elif len(sequence_count) == 0: ## initial case, when dict is empty
                sequence_count[eachdigit] = 1
                curr_key = eachdigit
            else:
                generated_string += str(sequence_count[curr_key]) + curr_key
                curr_key = eachdigit
                sequence_count.clear()
                sequence_count[eachdigit] = 1
        if len(sequence_count) > 0:
            generated_string += str(sequence_count[curr_key]) + curr_key
        return generated_string

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            sequence_elements = ['1']
            i = 0
            while len(sequence_elements) < n:
                sequence_elements.append(self.gen_number(sequence_elements[i]))
                i += 1
            print(sequence_elements)
            return sequence_elements[n - 1]

if __name__ == '__main__':
    sol = Solution()
    target = 5
    sol.countAndSay(target)