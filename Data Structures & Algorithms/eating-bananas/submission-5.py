class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        ceil(x/k) = time

        ceil(x/k) <= h

        h = max number of hours you have to eat all bananas
        k = minimum number bananas eaten per hour
        """
        piles = sorted(piles)

        left = 1
        right = max(piles)
        mini = right

        while left <= right:
            mid = (left + right) // 2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/mid)
            if time <= h:
                if mid < mini:
                    mini = mid
                right = mid - 1
            else:
                if mid+1 > mini:
                    break
                left = mid + 1
        return mini

 
        