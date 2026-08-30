class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        # check each row sepearately
        for i in range(n):
            arr = ['0']*10
            for j in range(n):
                if board[i][j] == '.':
                    continue
                el = int(board[i][j])
                if arr[el]!='0':
                    return False
                else:
                    arr[el]='@'
        
        # check each col sepearately
        for i in range(n):
            arr = ['0']*10
            for j in range(n):
                if board[j][i] == '.':
                    continue
                el = int(board[j][i])
                if arr[el]!='0':
                    return False
                else:
                    arr[el]='@'

        # check each 3x3 box
        for row in range(0, n, 3):
            for col in range(0, n, 3):
                arr = ['0'] * 10
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == '.':
                            continue
                        el = int(board[i][j])
                        if arr[el] != '0':
                            return False
                        arr[el] = '@'

        return True



