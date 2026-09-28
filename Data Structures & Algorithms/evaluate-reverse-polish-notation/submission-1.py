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

# I’ll use a stack to hold the numbers and intermediate results. I’ll go through the tokens from left to right. If a token is a number, I convert it to an integer and push it onto the stack.
# If it’s an operator, I pop two values. The first one I pop is the right operand, and the second is the left operand. I apply the operator and push the result back. At the end, the only value left in the stack is the answer.
# For division, the problem requires truncation toward zero. Python’s // rounds down for negative results, so I divide the absolute values first and then apply the correct sign.
# Each token is processed once, so the time complexity is O(n), and the stack uses O(n) space.