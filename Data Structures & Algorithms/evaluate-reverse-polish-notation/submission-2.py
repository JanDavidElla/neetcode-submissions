class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['*', '-', '+','/']
        stack = []
        for char in tokens:
            if char in operands:
                first = int(stack.pop())
                second = int(stack.pop())
                if char == '*':
                    stack.append(first * second)
                elif char == '-':
                    stack.append(second - first)
                elif char == '+':
                    stack.append(first + second)
                elif char == '/':
                    stack.append(second / first)
            else:
                stack.append(char)
        return int(stack.pop())