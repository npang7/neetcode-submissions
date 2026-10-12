class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        def backtrack(start):
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start,len(s)):
                part = s[start:end+1]
                if part != part[::-1]:
                    continue
                path.append(part)
                backtrack(end+1)

                path.pop()
                
        backtrack(0)
        return result
            