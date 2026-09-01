class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        car = sorted([[i,j] for position[i], position[j]])
        in loop:
        1. Add [0] by [1], remove boolean
        2. Check:
            - if >= target: remove
            - elif k < len(car) - 1 and current >= prior:
                    set to same as prior
            - else
        3. if remove then num += 1
        [1,2,3]
        [1,2]
        """
        cars = [0] * len(position)
        for i in range(len(position)):
            cars[i] = [position[i], speed[i]]

        stack = []
        for p, s in sorted(cars)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
