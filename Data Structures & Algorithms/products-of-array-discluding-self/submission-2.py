class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        numZero = 0
        zeroed = 1
        prod = 1
        for num in nums:
            if num == 0:
                zeroed = prod
                numZero += 1
            else:
                zeroed *= num
            prod *= num

        for i in range(len(nums)):
            element = nums[i]
            if numZero >= 2:
                nums[i] = 0
            elif element == 0:
                nums[i] = zeroed
            else:
                nums[i] = int(prod/element)
        return nums
        