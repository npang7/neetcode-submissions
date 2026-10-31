class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        count1 = [0] * 26
        count2 = [0] * 26
        res = []

        # count1 统计目标 p
        # count2 统计 s 的第一个窗口
        for i in range(len(p)):
            count1[ord(p[i]) - ord("a")] += 1
            count2[ord(s[i]) - ord("a")] += 1

        if count1 == count2:
            res.append(0)

        left = 0
        for r in range(len(p), len(s)):
            count2[ord(s[r]) - ord("a")] += 1
            count2[ord(s[left]) - ord("a")] -= 1
            left += 1
            if count1 == count2:
                res.append(left)

        return res