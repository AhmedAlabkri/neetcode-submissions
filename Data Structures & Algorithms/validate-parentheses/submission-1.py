class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {")": "(", "}":"{", "]":"["}
        # Do we have even elements?
        if (len(s) % 2) != 0:
            return False

        for char in s:
            if char in my_dict:
                if stack and stack[-1] == my_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False

    








        


            