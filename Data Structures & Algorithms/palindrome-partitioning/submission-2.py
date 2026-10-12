class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def backtrack(start):
            # 所有字符都已经分割完，保存当前方案
            if start == len(s):
                result.append(path.copy())
                return

            # 尝试下一段子串的不同结束位置
            for end in range(start, len(s)):
                part = s[start:end + 1] #end+1: Python 切片不包含右边界。要包含下标 end 的字符

                # 当前子串不是回文，跳过
                if part != part[::-1]:
                    continue

                # 1. 选择当前回文子串
                path.append(part)
                # 从这一段后面的字符继续分割
                backtrack(end + 1)

                # 2. 撤销这一层选择的子串
                path.pop()

        backtrack(0)
        return result