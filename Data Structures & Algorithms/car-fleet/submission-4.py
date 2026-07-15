class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))

        pair = sorted(pair, reverse = True)

        # [(7, 1), (4, 2), (1, 2), (0, 1)]

        # time = (target - position) / speed
        stack = []
        for i in range(len(pair)):
            time = (target - pair[i][0]) / pair[i][1]

            if stack:
                if stack[-1][1] < time:
                    stack.append((pair[i][0], time))
                else:
                    continue
            else:
                stack.append((pair[i][0], time))
        return len(stack)

        
