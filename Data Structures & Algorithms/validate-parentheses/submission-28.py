class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char not in my_dict:
                stack.append(char)
            else:
                if stack and stack[-1] == my_dict[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        