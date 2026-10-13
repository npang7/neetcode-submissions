class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:

        # index：接下来要匹配 word 中哪个位置的字符
        # node：当前走到的 Trie 节点
        def dfs(index, node):
            # 所有字符都匹配完了，检查是否为完整单词
            if index == len(word):
                return node.is_end

            char = word[index]

            # 点号可以匹配任意一个字母
            if char == ".":
                # 尝试当前节点的每一个子节点
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True

                # 所有分支都匹配失败
                return False

            # 普通字母：找不到对应子节点，匹配失败
            if char not in node.children:
                return False

            # 找到了这个字母，继续匹配下一个字符
            return dfs(index + 1, node.children[char])

        # 从根节点开始，先匹配 word[0]
        return dfs(0, self.root)
