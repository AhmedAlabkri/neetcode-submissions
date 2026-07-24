class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = None

        right = len(matrix) - 1 # last row
        left = 0 # first row

        while not left > right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                right = mid-1

            elif matrix[mid][0] < target:
                left = mid + 1

        # now bs the row
        if right < 0:
            return False
            
        row = matrix[right]

        right = len(row) - 1
        left = 0

        while not left > right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1

        return False
            
        

        