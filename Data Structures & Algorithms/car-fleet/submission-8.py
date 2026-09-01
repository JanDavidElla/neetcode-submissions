class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([[p, s] for p,s in zip(position, speed)], reverse=True) #Sorts cars from closest to farthest

        stack = []
        for p, s in cars:
            stack.append((target - p) / s) # Calculates time it takes to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
            #if the current time is less than the time on top of the stack
            
            # Whatever is on top of the stack is the TOA for the closer car. if it is not shorter than the one behind it, 
            # the one behind it beats it. Therefore, we keep the TOA of the closest car since they basically
            # travel in one unit.

            # If the current is longer than the one closer, then it never beats it.
            
                stack.pop()
        return len(stack)
