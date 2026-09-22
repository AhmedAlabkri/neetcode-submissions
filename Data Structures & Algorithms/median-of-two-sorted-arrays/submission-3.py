class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            B, A = A, B

        i = 0
        j = len(A) - 1

        while True:
            midA = (i + j) // 2
            midB = half - midA - 2

            Aleft = A[midA] if midA >= 0 else float("-inf")
            Aright = A[midA + 1] if midA+1 < len(A) else float("inf")
            Bleft = B[midB] if midB >= 0 else float("-inf")
            Bright = B[midB + 1] if midB+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 != 0:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            else:
                if Aleft > Bright:
                    # shrink A
                    j = midA - 1
                elif Bleft > Aright:
                    # extend A
                    i = midA + 1



