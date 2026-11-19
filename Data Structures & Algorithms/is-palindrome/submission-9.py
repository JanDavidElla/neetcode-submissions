class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach

        f = 0
        l = len(s) - 1

        while f < l:
            while f < l and not s[f].isalnum():
                f += 1
            while f < l and not s[l].isalnum():
                l -= 1
            if s[f].lower() != s[l].lower():
                return False
            f += 1
            l -= 1
        return True