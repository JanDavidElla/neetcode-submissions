class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = [];
        for i in range(len(nums)):
            num = nums[i]
            if(num in duplicate):
                return True
            else:
                duplicate.append(num)
        return False