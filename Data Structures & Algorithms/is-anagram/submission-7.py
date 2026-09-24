class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0) + 1
        for j in range(len(t)):
            if t[j] not in count or count[t[j]] == 0:
                return False
            if t[j] in count:
                count[t[j]] -= 1
        return True