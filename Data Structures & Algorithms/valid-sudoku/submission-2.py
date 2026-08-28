class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Use a dictionary
        BASICALLY
        
        dict with all numbers (0-9).
        If something like 0:2 => immediately return false

        for [i from 0 to 9][j from 0 to 2]
        - after i loop: check dict

        for [i from 0 to 2][j from 0 to 9]
        - after j loop: check dict

        for [i from 0 to 2] [j from 0 to 2] [l from 0 to 2]
        - picking 3x3 = i row = l * 3 + i, j row = l * 3 + j
        - after each l loop: check dict
        
        """
        #row
        nums = dict.fromkeys(range(10), 0)
        for j in range(9):
            for i in range(9):
                element = board[i][j]
                if element == ".":
                    continue
                nums[int(element)] += 1
            if any(value not in (0,1) for value in nums.values()):
                return False
            nums = dict.fromkeys(range(10),0)
        #col
        for j in range(9):
            for i in range(9):
                element = board[j][i]
                if element == ".":
                    continue
                nums[int(element)] += 1
            if any(value not in (0,1) for value in nums.values()):
                print(2)
                print(nums.values())
                return False
            nums = dict.fromkeys(range(10),0)    

        for l in range(3):
            rowMulti = l*3
            for c in range(3):
                colMulti = c*3
                for i in range(3):
                    for j in range(3):
                        element = board[i + rowMulti][j + colMulti]
                        if element == ".":
                            continue
                        nums[int(element)] += 1
                if any(value not in (0,1) for value in nums.values()):
                    print("3x3")
                    print(nums.values())
                    return False
                nums = dict.fromkeys(range(10),0)
        
        return True

        """
        [[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],       
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
        """
                    


