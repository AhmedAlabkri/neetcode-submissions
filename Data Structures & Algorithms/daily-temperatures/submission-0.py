class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)

        for i in range(len(temperatures)):
            counter = 0
            j = i
            while temperatures[i] >= temperatures[j]:
                counter += 1
                j += 1
                if j == len(temperatures):
                    counter = 0
                    break
            stack[i] = counter
        
        return stack
            




        