class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        path = []

        def backtrack(i):
            # 所有数字都已经选择了对应字母
            if i == len(digits):
                result.append("".join(path))
                return

            # 遍历当前数字对应的字母
            for letter in phone[digits[i]]:
                # 选择当前字母
                path.append(letter)

                # 继续处理下一个数字
                backtrack(i + 1)

                # 撤销当前层的选择
                path.pop()

        backtrack(0)
        return result

