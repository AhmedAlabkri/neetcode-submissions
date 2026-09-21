# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left) + 1
            right = dfs(curr.right) + 1

            self.result = max(self.result, left + right - 2)

            return max(left,right)
        dfs(root)
        return self.result