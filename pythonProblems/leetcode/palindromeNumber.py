class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(abs(x))[::-1] == str(abs(x)) if x < 0 else str(x)[::-1] == str(x)
