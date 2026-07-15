class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = [(30, 0), ]
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > stack[-1][0]:
                tempo, index = stack.pop(-1) # (tempo, i)
                result[index] = i - index
            
            stack.append((temperatures[i], i))

        return result


        