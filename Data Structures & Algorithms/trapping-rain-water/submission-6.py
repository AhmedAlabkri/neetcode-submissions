class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxL, maxR = height[i], height[j]
        result = 0
        while i < j:
            # min(maxL, maxR) - height[x] =

            minMax = min(maxL, maxR)

            if height[i] <= height[j]:
                result+= max(minMax-height[i], 0)
                i+=1
                maxL = max(maxL, height[i])
            else:
                result+= max(minMax-height[j], 0)
                j-=1
                maxR = max(maxR, height[j])
        return result