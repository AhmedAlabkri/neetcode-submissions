class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        L = 0
        R = len(A) - 1

        while True:
            PartiA = (L + R) // 2
            PartiB = half - PartiA - 2

            if PartiA < 0:
                Aleft = float("-infinity")
            else:
                Aleft = A[PartiA]

            if PartiA + 1 >= len(A):
                Aright = float("infinity")
            else:
                Aright = A[PartiA + 1]
            
            if PartiB < 0:
                Bleft = float("-infinity")
            else:
                Bleft = B[PartiB]

            if PartiB + 1 >= len(B):
                Bright = float("infinity")
            else:
                Bright = B[PartiB + 1]
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            else:
                if Aleft > Bright:
                    R = PartiA - 1                
                elif Bleft > Aright:
                    L = PartiA + 1
                    


