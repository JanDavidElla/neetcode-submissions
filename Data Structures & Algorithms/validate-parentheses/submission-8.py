class Solution:
    def isValid(self, s: str) -> bool:
        """
        variable: closing (dictates whether or not it needs a pair)

        """
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}

        for i in range(len(s)):
            if s[i] in pairs.keys():
                if len(stack) == 0:
                    return False
                if stack.pop() != pairs[s[i]]:
                    return False 
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        return False