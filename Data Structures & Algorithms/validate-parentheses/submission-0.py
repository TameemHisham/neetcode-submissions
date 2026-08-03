class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }
            
        for index, char in enumerate(s):
            if char in closeOpen:
                if stack and stack[-1] == closeOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) ==0:
            return True
        return False