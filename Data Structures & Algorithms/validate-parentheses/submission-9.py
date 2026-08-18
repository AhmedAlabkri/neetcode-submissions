class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        my_dict = {")": "(", "]":"[", "}":"{"}

        for char in s:
            if char not in my_dict:
                stack.append(char)
            else:
                if stack and my_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
