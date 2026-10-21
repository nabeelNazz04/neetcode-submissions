class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_seen=set()
            col_seen=set()
            for j in range(9):
                num_row=board[i][j]
                num_col=board[j][i]
                if num_row!='.':
                    if num_row not in row_seen:
                        row_seen.add(num_row)
                    else:
                        return False
                if num_col!='.':
                    if num_col not in col_seen:
                        col_seen.add(num_col)
                    else:
                        return False
        for box_row in range(3):
            for box_col in range(3):
                start_row=box_row*3
                start_col=box_col*3
                seen=set()
                for r in range(3):
                    for c in range(3):
                        num=board[start_row+r][start_col+c]
                        if num!='.':
                            if num not in seen:
                                seen.add(num)
                            else :
                                return False
        return True
