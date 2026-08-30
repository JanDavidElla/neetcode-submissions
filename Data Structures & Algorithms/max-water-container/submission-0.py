class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        keeps max variable
        2 pointers (left and right).
        - Calculates area.
        - smallest one:
            - if left is smallest: left ++
            - if right is smallest: right --
        keep going until left > right
        """
        maxH = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            a = h * w
            if a > maxH:
                maxH = a
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxH