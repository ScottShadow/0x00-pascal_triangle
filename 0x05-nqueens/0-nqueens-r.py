#!/usr/bin/python3
class Solution:

    def solveNQueens(self, n):
        col = set()
        neg_diag = set()
        pos_diag = set()
        res = []
        # board = [["."] * n for i in range(n)]
        board = []

        def bactrack(r):
            if r == n:
                # board_copy = ["".join(row)for row in board]
                board_copy = board.copy()
                print(f"appending {board}")
                res.append(board_copy)
                return
            for c in range(n):
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue

                col.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                board.append([r, c])
                # board[r][c] = "Q"

                bactrack(r+1)

                col.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
                # board[r][c] = "."
                board.pop()
        bactrack(0)
        return res


testSolution = Solution()

res = (testSolution.solveNQueens(6))
for i in res:
    print(i)
