class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        min = 0
        for i in range(1, len(prices)):
            left = prices[min]
            right = prices[i]

            if right < left:
                min = i
                continue

            window = right - left

            if window > currentMax:
                currentMax = window

        return currentMax


            