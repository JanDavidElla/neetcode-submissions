class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: #in the left sorted portion
                if target > nums[mid] or target < nums[left]: #if target after mid or target less than left
                    left = mid + 1
                else:
                    right = mid - 1
            else: #in the right sorted portion
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
