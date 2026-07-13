class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (tempo, index)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > stack[-1][0]:
                tempo, index = stack.pop(-1)
                result[index] = i - index

            stack.append((temperatures[i], i))
            
        return result


                
            # [30,38,30,36,35,40,28]
            # result = [1 , 4 , 1, 2, 1 , 0, 0]
            # stack = [(40, 5), (28, 6)]
            # i = 6 -> 28


        