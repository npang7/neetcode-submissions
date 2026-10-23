class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # 多创建一行和一列，用来表示空字符串
        # dp[i][j]表示两个字符串前i个和前j个字符的 LCS 长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # i 和 j 从 1 开始，表示字符串前缀的长度
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 当前字符相同：接在前一个前缀的 LCS 后面
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                #当前字符不同：跳过其中一个字符，取较大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 两个完整字符串的最长公共子序列长度
        return dp[m][n]