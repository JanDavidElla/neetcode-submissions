class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        two pointer: i and j
        i = first char, i++
        j = last char, j--
        while i < j:
            if i != j:
                return False
        return True

        """

        new_s = ("".join(char for char in s if char.isalnum())).lower()

        i = 0
        j = len(new_s) - 1

        while i < j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        return True