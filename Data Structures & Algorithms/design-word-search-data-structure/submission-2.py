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

    def search(self,word:str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end

            char = word[index]

            if char == ".":
                for child in node.children.values():
                    if dfs(index+1,child):
                        return True  #如果任何一个成功就返回true
                return False

                # 写法二：先拿到字母，再通过字母找到子节点
                # for char in node.children:
                #     child = node.children[char]

                #     if dfs(index + 1, child):
                #         return True
                # return False

            if word[index] not in node.children:
                return False

            return dfs(index + 1, node.children[char])

        return dfs(0, self.root)

# 中文思路清单
#
# 1. 定义 TrieNode，表示前缀树中的一个节点。
#    - children 是字典：字母 → 对应的子节点。
#    - is_end 表示是否有一个完整单词在当前节点结束。
#    - 新节点的 children 为空，is_end 初始为 False。
#
# 2. 初始化 WordDictionary。
#    - 创建根节点：self.root = TrieNode()。
#    - 根节点不代表任何字母，是所有单词的共同起点。
#    - TrieNode 是类，TrieNode() 才会创建一个节点对象。
#
# 3. addWord：逐个字母插入单词。
#    - 设置 node = self.root，从根节点开始。
#    - 遍历 word 中的每个 char。
#    - 如果 char 不在 node.children 中，就创建对应的子节点。
#    - 执行 node = node.children[char]，移动到下一层。
#    - 所有字母处理完后，设置 node.is_end = True。
#    - 结束标记放在循环外，只标记完整单词的结尾。
#    - 相同前缀使用已有节点，不需要重复创建。
#
# 4. search：使用 DFS，处理普通字母和点号。
#    - 定义辅助函数 dfs(index, node)。
#    - index 表示接下来要匹配 word 中哪个位置的字符。
#    - node 表示已经匹配完前 index 个字符后，当前所在的节点。
#    - 从 dfs(0, self.root) 开始搜索，并返回它的结果。
#    - 每匹配一个字符，就移动到子节点，并让 index 加 1。
#
# 5. DFS 的结束条件：index == len(word)。
#    - 说明搜索字符串中的所有字符都已经匹配完了。
#    - 返回 node.is_end，判断这里是否为完整单词的结尾。
#    - 路径存在，不代表完整单词存在。
#    - 例如只添加了 "day"，搜索 "da" 仍然应该返回 False。
#
# 6. 取出当前字符：char = word[index]。
#    - 如果 char == "."，就尝试当前节点的所有子节点。
#    - 使用 node.children.values()，拿到子节点对象，而不是字母键。
#    - 对每个 child，调用 dfs(index + 1, child)。
#    - 点号恰好匹配一个字母，所以必须移动一层，并让 index 加 1。
#    - 只要某个分支返回 True，就立即返回 True。
#    - 如果所有分支都失败，再返回 False。
#    - 这个 return False 必须放在 for 循环外，不能只试一个分支就放弃。
#
# 7. 如果 char 是普通字母，就沿指定分支继续搜索。
#    - 如果 char 不在 node.children 中，直接返回 False。
#    - 否则返回 dfs(index + 1, node.children[char])。
#    - 必须返回递归结果，让成功或失败传回上一层。
#    - 这里不需要修改节点，也不需要 path.pop() 或恢复访问标记。
#
# 8. 时间和空间复杂度。
#    - 令 L 为当前输入字符串的长度，d 为搜索字符串中的点号数量。
#    - addWord 时间为 O(L)，最多新增 O(L) 个节点。
#    - search 没有点号时，时间为 O(L)。
#    - 有点号时，每个点号最多尝试 26 个子节点。
#    - search 的最坏时间上界为 O(L * 26^d)，本题 d 最多为 2。
#    - search 的额外空间为 O(L)，来自递归调用栈。
#    - 分支逐个搜索，调用栈只保存当前路径。
#    - 整棵 Trie 的存储空间为 O(N)，N 是创建的节点总数。
#    - N 最多为所有添加单词的长度之和，再加一个根节点。
#
# 快速记忆思路
#
# 建树存词，逐字 DFS。
# 普通字母：找指定孩子。
# 遇到点号：试所有孩子。
# 一个成功：立即返回 True。
# 全部失败：返回 False。
# 字符走完：检查 is_end。
#
# 口语讲述思路
#
# I'll use a trie to store the words.
# Each node has a dictionary of children and a flag called is_end.
# This flag tells me whether a complete word ends at that node.
#
# To add a word, I start at the root and go through its letters.
# If a child node doesn't exist, I create it.
# Then I move to that child.
# After the last letter, I mark the node as the end of a word.
#
# For searching, I'll use DFS with an index and the current node.
# The index tells me which character I need to match next.
# I start with index zero at the root.
#
# If the index reaches the end of the search string, I return is_end.
# This makes sure I'm matching a complete word, not just a prefix.
#
# If the current character is a dot, I try every child node.
# For each child, I move to the next character and continue the search.
# Each dot matches exactly one letter.
# If any branch succeeds, I return true.
# I only return false after all the branches fail.
#
# For a regular letter, I look for its child node.
# If it's missing, I return false.
# Otherwise, I move to that child and search the rest of the word.
#
# Let L be the word length and d be the number of dots.
# Adding a word takes O(L) time.
# Searching without dots also takes O(L) time.
# With dots, the worst-case time is O(L times 26 to the power of d).
# The recursion stack uses O(L) extra space.

# node.children 和 node.children.values() 的区别
#
# 1. node.children 是字典。
#    - 键：字母。
#    - 值：对应的子节点对象。
#    - 例如：{"a": node_a, "b": node_b}
#    - node.children["a"] 可以拿到 node_a。
#
# 2. 直接遍历 node.children，得到的是键，也就是字母。
#    for char in node.children:
#        child = node.children[char]
#
# 3. 遍历 node.children.values()，得到的是值，也就是子节点对象。
#    for child in node.children.values():
#        # child 可以直接用于递归搜索。
#
# 4. 遇到 "." 时，需要尝试所有子节点。
#    - dfs 的第二个参数需要节点对象，所以使用 .values()。
#    for child in node.children.values():
#        if dfs(index + 1, child):
#            return True
#    return False
#
# 快速记忆：
# 遍历字典 → 拿到字母。
# 字典[字母] → 拿到对应节点。
# 遍历 .values() → 直接拿到所有子节点。
