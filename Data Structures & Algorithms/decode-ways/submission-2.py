class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i]：前 i 个字符的合法解码方式数量
        dp = [0] * (n + 1)

        # 空字符串作为起点，记为一种方式
        dp[0] = 1

        # 第一个字符只有不是 0，才能单独解码
        if s[0] != "0": 
            dp[1] = 1
        #如果第一个字符是 "0"，它不能单独对应任何字母，
        #dp[1] 就保持初始值 0。

        
        # 从前 2 个字符开始，计算到整个字符串
        for i in range(2, n + 1):

            # 情况一：最后取一个数字
            one_digit = int(s[i-1:i])
            if one_digit != 0:
                dp[i] += dp[i - 1]

            # 情况二：最后取两个数字
            two_digits = int(s[i - 2:i])

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

        s = "0122"