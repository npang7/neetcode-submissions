#在网格中进行回溯搜索
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: #word为空
            return True
        if not board or not board[0]: #board为空
            return False

        rows = len(board)
        cols = len(board[0])
        visited = set() # 保存当前路径已经使用过的格子

        def backtrack(r, c, i):
            # 当前格子越界
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # 当前格子已使用，或者字符不匹配
            if (r, c) in visited or board[r][c] != word[i]:
                return False
            # 当前字符匹配，而且已经是单词的最后一个字符。我们想要的结果！
            if i == len(word) - 1:
                return True

            # 选择当前格子
            visited.add((r, c))
            # 尝试从四个方向匹配下一个字符
            found = (
                backtrack(r + 1, c, i + 1)      # 下
                or backtrack(r - 1, c, i + 1)   # 上
                or backtrack(r, c + 1, i + 1)   # 右
                or backtrack(r, c - 1, i + 1))  # 左
            # 撤销选择，让其他路径可以使用这个格子
            visited.remove((r, c))

            return found  #四个方向中：
                            # - 任何一个成功，found 就是 True。
                            # - 全部失败，found 才是 False。
        
        # 主函数内容：
        # 每个格子都可能是单词的起点
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0): #只要有一个(r,c)为起点成功即可
                    return True

        return False

# 快速记忆：
# 状态：当前格子 (r, c)，当前字符下标 i。
# 越界、已使用、字符不匹配：False。
# 当前字符匹配，而且是最后一个字符：True。
# 选择：visited.add((r, c))。
# 探索：上下左右，匹配 i + 1。
# 撤销：visited.remove((r, c))。
# 返回四个方向的搜索结果。
# 外层遍历所有格子，分别尝试作为起点。

