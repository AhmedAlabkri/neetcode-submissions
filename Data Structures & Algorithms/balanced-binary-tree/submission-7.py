# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #self.leftTotal = 0
        #self.rightTotal = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        
        if not root:
            return True
        left = dfs(root.left)
        right = dfs(root.right)

        if left == -1 or right == -1:
            return False
            
        return dfs(root) != -1

        

            

            