class Solution: #中心扩展法（Expand Around Center）
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # 记录目前找到的最长回文的起点和长度
        # 题目保证字符串非空，所以先用第一个字符作为答案
        best_start = 0
        best_len = 1

        # 返回以 left、right 为中心扩展得到的回文边界
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # 指针已经越过合法回文的边界，需要向内退一格
            return left + 1, right - 1

        for i in range(n):
            # 1. 情况一：奇数长度，中心是一个字符
            left, right = expand(i, i)
            current_len = right - left + 1 
            #左右边界都包含在回文里，所以要加 1

            if current_len > best_len:
                best_start = left
                best_len = current_len

            # 2. 情况二：偶数长度，中心在两个字符之间
            left, right = expand(i, i + 1)
            current_len = right - left + 1

            if current_len > best_len:
                best_start = left
                best_len = current_len

        # 切片的结束位置不包含在结果中
        return s[best_start:best_start + best_len]