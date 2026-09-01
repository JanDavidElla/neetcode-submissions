class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        [5,1,2,3,4]
        [4,5,1,2,3]
        """
        left = 0
        right = len(nums) - 1

        
        smallest = nums[0]
        while left <= right:
            if nums[left] < nums[right]: #Found a sorted sub array. First element always give smallest
                smallest = min(nums[left], smallest)
                break
            mid = (left + right) // 2
            smallest = min(smallest, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
             
        return smallest