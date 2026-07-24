class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        raws = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                if val in raws[r]:
                    return False
                raws[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                box_id = (r // 3)*3 + (c // 3)

                if val in boxs[box_id]:
                    return False
                boxs[box_id].add(val)

        return True