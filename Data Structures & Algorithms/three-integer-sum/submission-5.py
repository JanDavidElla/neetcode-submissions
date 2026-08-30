class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        copy = []
        
        """
        -4 -1 -1 0 1 2

        1. Sort first
        keep a list keeping track of ones already seen.
        1. i loop
        2. i = target, then do regular Two Sum from i+1 to len(nums) - 1

        """

        for i in range(len(nums) - 2):
            if nums[i] in copy:
                continue
            target = 0 - nums[i] 
            #Regular two sum
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sumz = nums[left] + nums[right]
                if sumz == target:
                    newThing = [nums[i], nums[left], nums[right]]
                    if newThing not in output:
                        output.append(newThing)
                if sumz < target:
                    left += 1
                else:
                    right -= 1
            copy.append(nums[i])
        return output
