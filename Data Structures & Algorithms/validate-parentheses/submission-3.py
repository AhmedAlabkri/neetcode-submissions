class Solution:
    def isValid(self, s: str) -> bool:

        if (len(s)) % 2 != 0:
            return False

        my_dict = {")":"(", "]":"[", "}":"{"}

        # "([{}])"
        stack = []


        for char in s:
            if char in my_dict:
                if not stack or my_dict[char] != stack[-1]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True

            

            