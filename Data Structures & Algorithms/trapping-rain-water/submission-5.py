class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1

        result = 0
        maxL = height[i]
        maxR = height[j]
        while i < j:

            minMax = min(maxL, maxR)
            
            if height[i] <= height[j]:
                r = minMax - height[i]
                if r < 0:
                    pass
                else:
                    result += r
                i+=1
                maxL = max(maxL, height[i])
            else:
                r = minMax - height[j]
                if r < 0:
                    pass
                else:
                    result += r
                j-=1
                maxR = max(maxR, height[j])

        return result

