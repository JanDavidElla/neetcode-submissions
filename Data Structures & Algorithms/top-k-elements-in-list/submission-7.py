class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Variable: most
        FIFO 
        WE have a list of length k
        We iterate through nums
        -   Variable: counter

        -------------------------

        dict
        We iterate through nums:
        dict[nums] += 1 (O(n))

        I could iterate through dict
        - fill a list of size k
        - if value > most, add to list and update
        - if size > k, evict from list
        
        """

        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
                continue
            numDict[num] = 1
        

        most = 0
        numlist = []
        # ($, $$, $$$)
        newDict = sorted(numDict.items(), key=lambda item: item[1], reverse=True)
        for i, (key, value) in enumerate(newDict):
            if len(numlist) == k:
                break
            numlist.append(key)

    
        return numlist