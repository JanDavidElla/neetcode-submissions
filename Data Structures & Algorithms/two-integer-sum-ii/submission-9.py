class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        so basically,
        pointer left, pointer right
        add elements of those indexes
        if less than target, left += 1
        else: right -= 1
        """
        left = 0
        right = len(numbers) - 1
        while left < right: 
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
            