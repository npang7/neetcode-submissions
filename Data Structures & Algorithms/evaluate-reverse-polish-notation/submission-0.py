class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                # 整数除法，向 0 截断
                result = abs(left) // abs(right)
                if (left < 0) != (right < 0): #符号不同，所以result取负值
                    result = -result

            stack.append(result)

        return stack[0]