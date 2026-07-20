class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # (index, height[i])
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                width = i - index
                maxArea = max(maxArea, width * height)
                start = index

            stack.append((start, h))


        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, width * h)
        
        return maxArea







        