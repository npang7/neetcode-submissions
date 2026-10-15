class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        # 把与边界相连的 O 临时标记成 T
        def dfs(r, c):
            # 越界，或者当前不是 O，停止搜索
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"):
                return

            # 标记当前格子，表示需要保留
            board[r][c] = "T"

            # 继续寻找相连的 O
            dfs(r - 1, c)  # 上
            dfs(r + 1, c)  # 下
            dfs(r, c - 1)  # 左
            dfs(r, c + 1)  # 右

        # 从左右边界开始搜索
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # 从上下边界开始搜索
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # 替换被包围的 O，并恢复 T
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"