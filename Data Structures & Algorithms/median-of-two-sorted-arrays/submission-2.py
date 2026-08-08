class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        L = 0
        R = len(A) - 1

        while True:
            midA = (L + R) // 2
            midB = half - midA - 2

            if midA < 0:
                Aleft = float("-infinity")
            else:
                Aleft = A[midA]

            if midA + 1 >= len(A):
                Aright = float("infinity")
            else:
                Aright = A[midA + 1]

            if midB < 0:
                Bleft = float("-infinity")
            else:
                Bleft = B[midB]

            if midB + 1 >= len(B):
                Bright = float("infinity")
            else:
                Bright = B[midB + 1]

            
            if Aleft <= Bright and Bleft <= Aright:
                # even or  odd
                if total % 2 != 0:
                    return min(Bright, Aright)
                else:
                    return (min(Bright, Aright) + max(Aleft, Bleft)) / 2
            else:
                if Aleft > Bright:
                    R = midA - 1
                elif Bleft > Aright:
                    L = midA + 1




        