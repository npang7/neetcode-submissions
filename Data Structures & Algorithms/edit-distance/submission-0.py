class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j]：
        # word1 的前 i 个字符变成 word2 的前 j 个字符的最少操作数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 变成空字符串：全部删除
        for i in range(m + 1):
            dp[i][0] = i

        # 从空字符串变成目标：全部插入
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 最后的字符相同，直接保留
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 最后的字符不同，选择代价最小的操作
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # 删除
                        dp[i][j - 1],      # 插入
                        dp[i - 1][j - 1]   # 替换
                    )

        return dp[m][n]