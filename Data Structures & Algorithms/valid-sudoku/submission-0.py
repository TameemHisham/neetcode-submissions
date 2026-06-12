class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for el in row:
                if el == ".": continue
                if el in seen: return False
                seen.add(el)

        for col in range(9):
            seen = set()
            for row in range(9):
                el = board[row][col]
                if el == ".": continue
                if el in seen: return False
                seen.add(el)

        
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        el = board[r][c]
                        if el == ".": continue
                        if el in seen: return False
                        seen.add(el)

        return True
            
