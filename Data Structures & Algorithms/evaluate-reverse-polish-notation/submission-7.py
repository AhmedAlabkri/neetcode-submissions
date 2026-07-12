class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        # ["1","2","+","3","*","4","-"]
        # stack = [3, 3]
        # result = 3
        for i in range(len(tokens)):
            if tokens[i] == "+":
                #
                result = stack[-1] + stack[-2]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)

            elif tokens[i] == "-":
                #
                result = stack[-2] - stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)

            elif tokens[i] == "*":
                #
                result = stack[-2] * stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)

            elif tokens[i] == "/":
                #
                result = stack[-2] / stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(int(result))

            else:
                stack.append(int(tokens[i]))

        return stack[-1]


        