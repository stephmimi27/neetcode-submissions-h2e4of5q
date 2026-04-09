# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        sum = [root.val]

        def dfs(root): #runs through the function
            if not root:
                return 0
            
            #give left
            leftm = dfs(root.left)
            #give right
            rightm = dfs(root.right)

            leftm = max(leftm, 0) #step to avoid negatives
            rightm = max(rightm, 0)

            sum[0] = max(sum[0], root.val + leftm + rightm)
            return root.val + max(leftm, rightm)

           
        dfs(root)
        return sum[0]
        