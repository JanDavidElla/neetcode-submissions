class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stack = [] #will contain pairs [temp, index]

        for i, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                comp = stack.pop()
                output[comp[1]] = i - comp[1]
            stack.append([elem, i])
        return output

