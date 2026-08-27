class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {"}":"{", "]":"[", ")":"("}
        stack = []


        for char in s:
            if char not in my_dict:
                stack.append(char)
            else:
                if stack and stack[-1] == my_dict[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        
        return False
