class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        path = []
        result = []
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
        def backtrack(i):
            if i == len(digits): ##注意不是len-1，要多循环一次才到终止条件！！
                result.append("".join(path))
                return
            for letter in phone[digits[i]]:
                path.append(letter)
                backtrack(i+1)
                path.pop()
                
        backtrack(0)
        return result