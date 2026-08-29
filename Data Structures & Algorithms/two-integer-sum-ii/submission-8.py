class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        i | i + 1 .... n

        binary search

        while first != second
            first = i + 1
            second = len(numbers) - 1
            middle = (first + second) / 2
            if bruh = target - numbers[i] == numbers[middle]: return [i, middle]
            if numbers[middle] > bruh:
                first = middle + 1
            else:
                second = middle
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
            