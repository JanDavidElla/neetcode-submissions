class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 * 2 * 4 * 6
        basically compute the the product of everything
        replace nums[i] with product/nums[i]

        edge case: when there is one zero
        - You need another variable containing the product of everything except for that 0


        """
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

        """
        Normal case (no 0s): prod/element
        Edge case 1 (one 0): if 0, put in zeroed. Else, put in 0 (prod)
        Edge case 2 (two or more 0s): just put 0
        """
        for i in range(len(nums)):
            element = nums[i]
            if numZero >= 2:
                nums[i] = 0
            elif element == 0:
                nums[i] = zeroed
            else:
                nums[i] = int(prod/element)
        return nums
        