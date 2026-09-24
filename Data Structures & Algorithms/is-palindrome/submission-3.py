class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []

        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())

        return cleaned == cleaned[::-1]