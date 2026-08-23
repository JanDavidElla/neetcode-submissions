class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        put each character in a list, sort them, compare
        """
        if len(s) != len(t) or s is None or t is None:
            return False

        seen_s = {}
        seen_t = {}
        for i in range(len(s)):
            if s[i] in seen_s:
                seen_s[s[i]] += 1
            else:
                seen_s[s[i]] = 1
            if t[i] in seen_t:
                seen_t[t[i]] += 1
            else:
                seen_t[t[i]] = 1
        return seen_s == seen_t