class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def backtrack(open_count, close_count):
            # 停止条件：左右括号都已使用 n 个，保存当前字符串
            if open_count == n and close_count == n:
                result.append("".join(path))
                return

            # 左括号还没用完，可以加入一个左括号
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop() # 撤销当前层加入的左括号

            # 存在尚未匹配的左括号，可以加入一个右括号
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop() # 撤销当前层加入的右括号


        backtrack(0, 0)
        return result