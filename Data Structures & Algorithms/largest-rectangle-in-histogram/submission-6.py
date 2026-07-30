class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # (start, height[i])
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()

                maxArea = max(maxArea, (i - index) * height)
                start = index
            
            stack.append((start, heights[i]))
        

        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, width * h)

        return maxArea



        