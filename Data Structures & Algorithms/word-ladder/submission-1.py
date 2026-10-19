from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 保存尚未访问的合法单词，方便快速查找
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        # 保存：(当前单词, 到达它的序列包含多少个单词)
        queue = deque([(beginWord, 1)])

        # 起点已经访问，移除，避免之后又回到起点
        word_set.discard(beginWord)

        while queue:
            word, word_count = queue.popleft()

            if word == endWord:
                return word_count

            # 尝试修改每一个位置
            for i in range(len(word)):

                # 尝试把这个位置换成其他字母
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter == word[i]:
                        continue

                    # 修改位置左边的部分 + 新字母 + 修改位置右边的部分
                    next_word = word[:i] + letter + word[i + 1:]

                    # 只考虑合法且尚未访问的单词
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, word_count + 1))

        return 0
# 中文思路清单（Word Ladder：BFS + 逐个位置替换字母）
#
# 1. 把单词转换问题看成图中的最短路径问题。
#    - 每个单词是一个节点。
#    - 两个单词恰好有一个位置的字母不同，就可以一步转换。
#    - 每次转换的代价相同，因此使用 BFS 找最短转换序列。
#    - 返回的是序列中的单词数量，包括起点和终点，不是转换次数。
#    - 例如 cat → bat → bag → sag，转换 3 次，但答案是 4。
#
# 2. 把词表转换成集合，并检查目标单词。
#    - word_set = set(wordList)。
#    - 使用集合，方便快速判断生成的单词是否在词表中。
#    - word_set 同时保存“合法且尚未访问”的单词。
#    - 如果 endWord 不在 word_set 中，直接返回 0。
#    - 因为每次转换得到的单词都必须在词表中，目标单词也不例外。
#
# 3. 初始化 BFS 队列，并标记起点已经访问。
#    - queue = deque([(beginWord, 1)])。
#    - 队列保存：(当前单词, 到达它的序列包含多少个单词)。
#    - 初始序列只有 beginWord，所以计数从 1 开始。
#    - word_set.discard(beginWord)：防止之后重复访问起点。
#    - beginWord 不一定在词表中，discard 在元素不存在时不会报错。
#
# 4. 只要队列不为空，就继续搜索。
#    - word, word_count = queue.popleft()。
#    - word：当前处理的单词。
#    - word_count：从起点到当前单词，序列中的单词数量。
#    - 使用 popleft，而不是 pop，保证先入队的方案先处理。
#    - BFS 会先处理较短的序列，再处理较长的序列。
#
# 5. 如果当前单词是目标，立即返回。
#    - if word == endWord: return word_count。
#    - 因为 BFS 按序列长度逐层搜索，第一次到达目标就是最短答案。
#    - return 会立即结束整个函数。
#
# 6. 尝试修改当前单词的每一个位置。
#    - 外层循环：for i in range(len(word))。
#    - i 表示准备修改的字符下标。
#    - 内层循环：遍历 a 到 z，尝试不同的替换字母 letter。
#    - 如果 letter == word[i]，跳过。
#    - 因为换成原来的字母，没有发生变化，不符合恰好改变一个字母。
#
# 7. 构造只修改一个位置的新单词。
#    - next_word = word[:i] + letter + word[i + 1:]。
#    - word[:i]：修改位置左边的部分，不包含下标 i。
#    - letter：替换后的新字母。
#    - word[i + 1:]：修改位置右边的部分。
#    - 例如 word = "cat"，i = 0，letter = "b"：
#      next_word = "" + "b" + "at" = "bat"。
#    - Python 字符串不能直接修改，所以需要构造一个新字符串。
#
# 8. 如果新单词合法且尚未访问，就标记并入队。
#    - if next_word in word_set。
#    - 条件成立，说明它在词表中，并且还没有被发现过。
#    - word_set.remove(next_word)：立即标记已经访问。
#    - queue.append((next_word, word_count + 1))。
#    - 新序列在当前序列后面增加一个单词，所以计数加 1。
#    - 从集合中删除，能够防止其他路线把同一个单词重复加入队列。
#    - 这里已经确认元素存在，因此可以安全使用 remove。
#
# 9. 如果队列为空，仍然没有找到目标，返回 0。
#    - 队列为空，说明所有能够到达的单词都检查过了。
#    - 目标虽然可能在词表中，但不一定存在合法路线能够到达它。
#    - 没有转换序列时返回 0，不是 -1。
#
# 10. 容易混淆的地方。
#     - beginWord 不必在 wordList 中，后续转换得到的单词必须在。
#     - 计数从 1 开始，因为答案包含起始单词。
#     - 一次只能修改一个位置，其他位置必须保持不变。
#     - word_set 中删除单词，相当于记录 visited，不需要额外创建集合。
#     - 删除 word_set 中的元素，不会修改原来的 wordList。
#     - 普通 BFS 每次转换代价相同，首次入队就可以标记访问。
#     - 不要照搬 Dijkstra 的处理方式，等到出队才标记。
#     - 本题每一步代价相同，使用普通队列即可，不需要最小堆。
#
# 11. 时间和空间复杂度。
#     - 设词表中有 N 个单词，每个单词长度为 L。
#     - 每个单词最多入队一次，连同起点，最多处理 N + 1 个单词。
#     - 每个单词有 L 个位置，每个位置最多尝试 26 个字母。
#     - 每次切片、拼接新单词，以及计算新字符串的哈希，都需要 O(L) 时间。
#     - 时间复杂度：O(N × 26 × L²)，简化为 O(NL²)。
#     - 空间复杂度：O(NL)。
#     - 集合和队列最多保存 O(N) 个单词，队列中的新字符串长度为 L。
#
# 快速记忆思路
# 单词当节点，一次改一个字母找邻居。
# 词表转集合，队列从 (beginWord, 1) 开始。
# 合法单词：从集合删除，再带着计数加 1 入队。
# BFS 首次到达目标，返回单词数量；队列为空还没找到，返回 0。
#
# 口语讲述思路
#
# I'll treat each word as a node in a graph.
# Two words are connected if they differ at exactly one position.
# Since every transformation has the same cost, I'll use BFS.
#
# First, I put the word list into a set for fast lookups.
# If the end word isn't in the set, I return zero.
#
# The queue stores a word and the number of words in its sequence.
# I start with the begin word and a count of one.
#
# For each word, I try replacing each character with every lowercase letter.
# If the new word is in the set, it's a valid, unvisited neighbor.
# I remove it from the set right away to avoid adding it more than once.
# Then I add it to the queue with the count increased by one.
#
# BFS explores shorter sequences first.
# So when I reach the end word, I return the current count.
# If the queue becomes empty without finding it, I return zero.
#
# Let N be the number of words and L be the word length.
# The time complexity is O(N times L squared),
# because creating and hashing each candidate word takes O(L) time.
# The space complexity is O(N times L) for the set and the queue.
