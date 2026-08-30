class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '/':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(char))
        return stack.pop()