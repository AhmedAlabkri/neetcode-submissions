class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (indexStart, h)
        maxRec = 0
        for i in range(len(heights)):

            indexStart = i
            while stack and stack[-1][1] > heights[i]:
                index, h = stack.pop()
                maxRec = max(maxRec, h * (i - index))
                indexStart = index
            stack.append((indexStart, heights[i]))

        for t in stack:
            maxRec = max(maxRec, t[1] * (len(heights) - t[0]))
        return maxRec
