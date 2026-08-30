class Solution:
    def isValid(self, s: str) -> bool:
        """
        variable: closing (dictates whether or not it needs a pair)

        """
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}

        for i in range(len(s)):
            if s[i] in pairs:
                if stack and stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        return False