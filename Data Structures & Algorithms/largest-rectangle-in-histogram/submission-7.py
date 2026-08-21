class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [(startIndex, height)]
        maxSize = 0


        for i in range(len(heights)):

            startIndex = i

            while stack and stack[-1][1] > heights[i]:
                index, height= stack.pop()

                maxSize = max(maxSize, (i - index) * height)
                startIndex = index

            stack.append((startIndex, heights[i]))

        
        for i, h in stack:
            maxSize = max(maxSize, (len(heights) - i) * h)

        return maxSize




