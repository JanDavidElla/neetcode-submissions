class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['*', '-', '+','/']
        stack = []
        for char in tokens:
            if char in operands:
                first = stack.pop()
                second = stack.pop()
                if char == '*':
                    stack.append(first * second)
                elif char == '-':
                    stack.append(second - first)
                elif char == '+':
                    stack.append(first + second)
                elif char == '/':
                    stack.append(int(second / first))
            else:
                stack.append(int(char))
        return stack.pop()