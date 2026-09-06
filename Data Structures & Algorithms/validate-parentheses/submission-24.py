class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {"}":"{","]":"[",")":"("}

        for char in s:
            if char not in mydict:
                stack.append(char)
            else:
                if stack and stack[-1] == mydict[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False