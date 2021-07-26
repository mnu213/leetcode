class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            else:
                if len(stack):
                    temp = stack.pop()
                else:
                    return False
                if (temp == '{' and char == '}') or (temp == '(' and char == ')') or (temp == '[' and char == ']'):
                    continue
                else:
                    return False
        if len(stack):
            return False
        else:
            return True
