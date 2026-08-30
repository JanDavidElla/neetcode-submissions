class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        We keep a stack,
        basically it adds to the stack
        if the stack is not empty, it will compare with current element

        ex:
        Input: temperatures = [30,38,30,36,35,40,28]

        Output: [1,4,1,2,1,0,0]
        """
        output = [0] * len(temperatures)
        stack = [] #will contain pairs [temp, index]

        for i, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                comp = stack.pop()
                output[comp[1]] = i - comp[1]

            stack.append([elem, i])
        return output

