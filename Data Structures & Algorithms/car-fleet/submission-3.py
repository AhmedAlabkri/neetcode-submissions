class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:



        pair = list(zip(position, speed))
        pair = sorted(pair, reverse = True)
        stack = []
        # position : [4,1,0,7]
        # speed  : [2,2,1,1]
        # pair  = [(7, 1), (4, 2), (1, 2), (0, 1)] , target = 10
        # stack = [(7, 3), ]
        #
        # formula: time = (target - position[i]) / speed[i]
        for i in range (len(pair)):
            time = (target - pair[i][0]) / pair[i][1]
            new_pair = (pair[i][0], time)

            if stack:
                if stack[-1][1] >= new_pair[1]:
                    continue
                elif stack[-1][1] < new_pair[1]:
                    stack.append(new_pair)
            else:
                stack.append(new_pair)

        return len(stack)



