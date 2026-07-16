class Solution:
    def trap(self, height: List[int]) -> int:


        i = 0
        j = len(height) - 1
        # for first step
        l_max = height[i]
        r_max = height[j]

        counter = 0
        while i < j:
            if l_max > r_max:
                j -= 1
                x = r_max - height[j]
                if x > 0:
                    counter += x
            
                r_max = max(height[j], r_max)

            elif l_max <= r_max:
                i += 1
                x = l_max
                x = x - height[i]
                if x > 0:
                    counter += x
            
                l_max = max(height[i], l_max)
        return counter




        