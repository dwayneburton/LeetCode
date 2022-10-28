# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        sorted_list = []
        sorted_list += self.inorderTraversal(root.left)
        sorted_list.append(root.val)
        sorted_list += self.inorderTraversal(root.right)
        return sorted_list