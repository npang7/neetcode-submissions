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

                    next_word = word[:i] + letter + word[i + 1:]

                    # 只考虑合法且尚未访问的单词
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, word_count + 1))

        return 0