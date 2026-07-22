class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # (index, height[i])
        max_Area = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                max_Area = max(max_Area, (height * (i - index)))

                start = index
            
            stack.append((start, heights[i]))
        
        for start, height in stack:
            width = len(heights) - start
            max_Area = max(max_Area, (height * width))

        
        return max_Area

            

            





        