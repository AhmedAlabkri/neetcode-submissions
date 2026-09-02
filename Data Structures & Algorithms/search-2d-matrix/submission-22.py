class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the middle sub-list
        # look up list[list[0]]
        # three conditions: 
        # 1- target   -> found it, return True
        # 2- < target -> target in the rigght lists.
        # 3- > target -> target in the left lists.
        # once we have one list, we binary search that list.

        i = 0
        j = len(matrix) - 1 #number of lists
        c = None
        while i <= j:
            mid = (i+j) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target <= matrix[mid][len(matrix[mid])-1]:
                c = mid
                break
            elif matrix[mid][0] < target:
                i = mid+1
            elif matrix[mid][0] > target:
                j = mid - 1
        
        if c == None:
            return False
        correctListIndex = c
        i = 0
        j = len(matrix[correctListIndex]) - 1
        while i <= j:
            mid = (i + j) // 2

            if matrix[correctListIndex][mid] == target:
                return True
            elif matrix[correctListIndex][mid] < target:
                i = mid+1
            else:
                j = mid-1
        return False


        





