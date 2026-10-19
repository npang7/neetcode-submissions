class Solution: #中心扩展法
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # 记录所有回文子串的总数量
        total = 0

        # 返回这个中心能够找到多少个回文子串
        def expand(left, right):
            count = 0

            while left >= 0 and right < n and s[left] == s[right]:
                # 当前区间是一个回文子串
                count += 1

                # 向两边继续扩展
                left -= 1
                right += 1

            return count

        for i in range(n):
            # 检查奇数长度的回文
            total += expand(i, i)

            # 检查偶数长度的回文
            total += expand(i, i + 1)

        return total