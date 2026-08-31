class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stack = []

        for i, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                stackTemp, stackIn = stack.pop()
                output[stackIn] = i - stackIn
            stack.append([elem, i])
        return output

