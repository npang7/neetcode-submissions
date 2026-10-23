class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        # 所有字符都必须恰好使用一次
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 两个空字符串可以拼出空字符串
        dp[0][0] = True

        for i in range(m + 1): #当前使用 s1 的前几个字符
            for j in range(n + 1): #当前使用 s2 的前几个字符
                # 最后一个字符来自 s1
                if i > 0 and s1[i - 1] == s3[i + j - 1]: #数组的index要-1
                    dp[i][j] = dp[i - 1][j]

                # 最后一个字符来自 s2
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[m][n]
        
# dp[i][j] 表示：
# s1 的前 i 个字符与 s2 的前 j 个字符，能否交错拼出 s3 的前 i + j 个字符。