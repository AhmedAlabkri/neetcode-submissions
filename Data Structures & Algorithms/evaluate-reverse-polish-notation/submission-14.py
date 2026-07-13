class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        # [5,3,2,"+"]
        # result = 5
        for i in tokens:
            if i == "+":
                result = stack[-1] + stack[-2]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            elif i == "-":
                result = stack[-2] - stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            elif i == "*":
                result = stack[-1] * stack[-2]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
            elif i == "/":
                result = stack[-2] / stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(int(result))

            else:
                stack.append(int(i))

        return int(stack[-1])
