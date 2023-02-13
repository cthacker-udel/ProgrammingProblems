from typing import List

class Solution:
    def any_available_letters(self, letter: str, available_letters: List[str], availability: dict(str, bool)) -> str:
        pass

    def repeatedLimitedString(self, s: str, repeatLimit: int) -> str:
        constructed_string = ""
        letters = sorted(set(s), reverse=True)
        letter_occurrence = [s.count(x) for x in letters]
        repeat_count = dict.fromkeys(letters, 0)
        for each_letter in s:
            
        return constructed_string


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedLimitedString("cczazcc", 3))
