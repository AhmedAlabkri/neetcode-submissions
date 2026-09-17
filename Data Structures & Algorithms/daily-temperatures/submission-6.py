class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = len(temperatures) * [0]
        stack = [] # (i, temp)

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                index, temp = stack.pop()
                result[index] = (i - index)
            stack.append((i, temperatures[i]))
        return result


