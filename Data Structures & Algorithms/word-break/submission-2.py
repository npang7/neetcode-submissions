class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for end in range(1, n+1):
            for word in wordDict:
                start = end - len(word)
                if start < 0:
                    continue
                if dp[start] and s[start:end] == word:
                    dp[end] = True
                    break
        return dp[n]
