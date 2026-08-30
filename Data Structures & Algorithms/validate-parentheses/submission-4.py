class Solution:
    def isValid(self, s: str) -> bool:
        """
        variable: closing (dictates whether or not it needs a pair)

        """
        closing = False
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}

        for i in range(len(s)):
            if i == len(s) - 1 and (s[i] == '(' or s[i] == '{' or s[i] == '['):
                return False

            if s[i] == ')':
                if len(stack) == 0:
                    return False
                if stack.pop() !=  '(':
                    return False
                continue
            if s[i] == '}':
                if len(stack) == 0:
                    return False
                if stack.pop() !=  '{':
                    return False
                continue
            if s[i] == ']':
                if len(stack) == 0:
                    return False
                if stack.pop() !=  '[':
                    return False
                continue
            stack.append(s[i])

        if len(stack) == 0:
            return True
        return False