class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        non-dereasing order

        plan:
        we can compare the first index of each matrix via binary search.
        if left == right, then we look at that array and implement binary search.

        [1,2],[3,4]
        """

        left = 0
        right = len(matrix) - 1

        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if matrix[mid+1][0] > target:
                    left = mid
                    break
                left = mid + 1
            else:
                right = mid - 1
        
        #reminder, if it is a regular 1D array
        second_matrix = matrix[left] 
        left = 0
        right = len(second_matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if second_matrix[mid] == target:
                return True
            elif second_matrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        #regular binary search