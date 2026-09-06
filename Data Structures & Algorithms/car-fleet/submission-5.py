class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = [] # (ArrivalTime, index)
        pair = []
        for i in range(len(position)):
            pair.append((position[i],speed[i]))

        pairs = sorted(pair, reverse=True)


        for pos, sp in pairs:
            AT = (target - pos) / sp
            if stack and stack[-1][0] < AT:
                stack.append((AT, pos))

            elif not stack:
                stack.append((AT, pos))
            
            
        return len(stack)

        # target = 10, position = [1,4], speed = [3,2]
        # stack = [] , pair = [(4, 2), (1, 3)]




