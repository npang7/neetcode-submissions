class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(
        self, board: List[List[str]], words: List[str]
    ) -> List[str]:

        # 1. 把所有候选单词加入前缀树
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            # 在单词结尾保存完整单词
            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        # node 表示匹配当前格子之前，所在的 Trie 节点
        def dfs(r, c, node):
            # 越界，停止搜索
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            char = board[r][c]

            # 当前字母无法继续匹配，停止搜索
            # 已访问格子的 "#" 也会在这里被排除
            if char not in node.children:
                return

            # 当前字母匹配成功，移动到对应子节点
            child = node.children[char]

            # 找到了一个完整单词
            if child.word is not None:
                result.append(child.word)

                # 清除结束标记，避免重复添加这个单词
                child.word = None

            # 标记当前格子已经在这条路径中使用过
            board[r][c] = "#"

            # 从当前格子继续向四个方向搜索
            dfs(r + 1, c, child)
            dfs(r - 1, c, child)
            dfs(r, c + 1, child)
            dfs(r, c - 1, child)

            # 回溯：恢复当前格子的原始字母
            board[r][c] = char

            # 如果这个分支已没有待查单词，就删除它
            if child.word is None and not child.children:
                del node.children[char]

        # 2. 尝试把棋盘上的每个格子作为起点
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result