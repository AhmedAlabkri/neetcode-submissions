class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # pairs: [8, 13, 40]

        # target > 8
        # target < 13
        # 13 , 1

        length = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if i == 0 and matrix[i][length] >= target:
                right = length
                left = 0
                while not left > right:
                    mid = (left + right) // 2

                    if matrix[i][mid] == target:
                        return True
                    
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    
                    elif matrix[i][mid] < target:
                        left = mid + 1

                break
            elif target <= matrix[i][length] and target > matrix[i-1][length] :

                right = length
                left = 0
                while not left > right:
                    mid = (left + right) // 2

                    if matrix[i][mid] == target:
                        return True
                    
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    
                    elif matrix[i][mid] < target:
                        left = mid + 1
                
                break
        return False



        
        

        


