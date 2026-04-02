class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = {}
            for num in row:
                if num == '.':
                    continue
                elif num in seen:
                    return False
                else:
                    seen[num] = 1

        for c in range(9):
            seen = {}
            for r in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                elif num in seen:
                    return False
                else:
                    seen[num] = 1

        for box_r in range(0, 9, 3):       # 0, 3, 6
            for box_c in range(0, 9, 3):   # 0, 3, 6
                seen = {}
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        num = board[r][c]
                        if num == '.':
                            continue
                        elif num in seen:
                            return False
                        else:
                            seen[num] = 1
            
        return True



