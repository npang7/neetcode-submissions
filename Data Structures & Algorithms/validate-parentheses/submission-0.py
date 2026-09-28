class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in closeToOpen:
                if not stack : #empty stack
                    return False
                if stack[-1] != closeToOpen[c]: #栈的右侧是栈顶 ["(", "[", "{"]
                                                #                        stack top         
                    return False

                stack.pop()
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False# empty stack is what i want    or # return not stack

# I use a stack because the most recently opened bracket must be closed first. I also create a dictionary that maps each closing bracket to its matching opening bracket.

# Then I go through the string one character at a time. If the current character is an opening bracket, I push it onto the stack. If it is a closing bracket, I first check whether the stack is empty. If it is, there is no opening bracket to match it, so I return `false`.

# Otherwise, I check whether the top of the stack is the matching opening bracket. If it matches, I pop it from the stack. If it does not match, I return `false`.

# After checking the entire string, I return `true` if the stack is empty, because that means all the brackets were matched correctly. Otherwise, I return `false`.

# The time complexity is O(n), and the space complexity is O(n).