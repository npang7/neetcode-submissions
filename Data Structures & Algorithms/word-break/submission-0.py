class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # dp[i]：前 i 个字符能否完整拆分
        dp = [False] * (n + 1)

        # 空字符串可以作为拆分的起点
        dp[0] = True

        # 从前 1 个字符开始，逐渐计算到整个字符串
        for end in range(1, n + 1):

            # 尝试让每个字典单词占据当前这段字符串的末尾
            for word in wordDict:
                start = end - len(word)

                # 单词太长，当前这段字符串放不下它
                if start < 0:
                    continue

                # 前面的部分可以拆分，后面的部分正好是这个单词
                if dp[start] and s[start:end] == word:
                    dp[end] = True
                    #break

        return dp[n]