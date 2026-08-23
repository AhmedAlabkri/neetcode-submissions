class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        stack = []
        for i in tokens:
            if i == "+":
                if stack:
                    output = stack[-2] + stack[-1]

                    stack.pop()
                    stack.pop()
                    stack.append(output)
            elif i == "-":
                if stack:
                    output = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(output)
            elif i == "*":
                if stack:
                    output = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(output)
            elif i == "/":
                if stack:
                    output = stack[-2] / stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(output))
            else:
                stack.append(int(i))
        return stack[-1]
