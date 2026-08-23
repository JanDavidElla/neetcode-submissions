class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        put each character in a list, sort them, compare
        """

        new_s = sorted(list(s))
        new_t = sorted(list(t))
        if new_s == new_t:
            return True
        return False