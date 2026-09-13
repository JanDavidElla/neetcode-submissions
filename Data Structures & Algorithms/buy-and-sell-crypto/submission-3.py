class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMax = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                window = prices[r] - prices[l]
                currentMax = max(currentMax, window)
            r = r + 1
        return currentMax



            