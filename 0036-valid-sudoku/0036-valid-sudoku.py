class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen=set()
            for col in range(9):
                value=board[row][col]
                if value==".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

        for col in range(9):
            seen=set()
            for row in range(9):
                value=board[row][col]
                if value==".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

        for row in range(0,9,3):
            for col in range(0,9,3):
                seen=set()
                for r in range(row,row+3):
                    for c in range(col, col+3):
                        value=board[r][c]
                        if value==".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)

        return True
                
        