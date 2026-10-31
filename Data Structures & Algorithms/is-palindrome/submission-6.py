class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        cleaned = "".join(chars)

        return cleaned == cleaned[::-1]
    
#这样更直观，只是需要 O(n) 额外空间保存加工后的字符串。