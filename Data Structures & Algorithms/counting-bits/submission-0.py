class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i]：数字 i 的二进制中 1 的数量
        dp = [0] * (n + 1)

        # 当前数字最高位的 1 代表的数值
        offset = 1

        for i in range(1, n + 1):
            # 到达下一个 2 的幂时，更新最高位的数值
            if offset * 2 == i:
                offset = i

            # 去掉最高位的 1，利用剩余数字的答案
            dp[i] = 1 + dp[i - offset]

        return dp