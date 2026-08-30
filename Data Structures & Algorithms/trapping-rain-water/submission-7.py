class Solution:
    def trap(self, height: List[int]) -> int:
        """
        left variable
        right variable

        if left matches right -> left moves
        - Basically, they are trying to match or beat each other's heights.

        1. left moves until it equates or beats right's height
            - if it finds anything below right, total += right's height - left's height
        2. right moves until it equates or beats left's height
            - if it finds anything below left, total += left's height - right's height
        """
        total = 0
        left = 0
        right = len(height) - 1

        
        while left < right:
            if height[left] < height[right]:
                copy = height[left]
                left += 1
                while height[left] < height[right]:
                    if left > right:
                        break
                    if height[left] <= copy:
                        total += copy - height[left]
                    if height[left] > copy:
                        copy = height[left]
                    left += 1


            copy = height[right]
            right -= 1
            while height[right] < height[left]:
                if right < left:
                    break
                if height[right] <= copy:
                    total += copy - height[right]
                
                if height[right] > copy:
                    copy = height[right]

                right -= 1
        
        return total

            



        """
[0,1,0,2,1,0,1,3,2,1,2,1]

       #
   #   ## #
_#_##_######  

    height of 3
    width of 5
    15

#
# #
###
###
        """