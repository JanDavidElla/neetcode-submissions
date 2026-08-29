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
        if len(numbers) == 2:
            return [1,2]

        for i in range(len(numbers)):
            
            num = target - numbers[i]
            first = i + 1
            second = len(numbers) - 1
            while first <= second:
                middle = (first + second) // 2
                if num == numbers[middle]:
                    return [i + 1, middle + 1]
                if numbers[middle] < num:
                    first = middle + 1
                else:
                    second = middle - 1
            