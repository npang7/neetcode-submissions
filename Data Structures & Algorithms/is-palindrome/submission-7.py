class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # 跳过左侧的非字母、非数字字符
            while left < right and not s[left].isalnum():
                left += 1

            # 跳过右侧的非字母、非数字字符
            while left < right and not s[right].isalnum():
                right -= 1

            # 忽略大小写后比较
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True