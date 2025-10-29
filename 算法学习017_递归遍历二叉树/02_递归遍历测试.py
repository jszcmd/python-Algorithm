""" 递归遍历二叉树:前序,中序和后序 """
# 前序遍历二叉树:
#   测试链接:https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
# 中序遍历二叉树:
#   测试链接:https://leetcode.cn/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=binary-tree
# 后序遍历二叉树:
#   测试链接:https://leetcode.cn/problems/binary-tree-postorder-traversal/

from typing import Optional, List


# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 前序遍历
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right

    # 中序遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

    # 后序遍历
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]
