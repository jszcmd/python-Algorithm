""" 二叉树的最大深度和最小深度 """
# 二叉树的最大深度:
#   测试链接:https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
# 二叉树的最小深度:
#   测试链接:https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/

from typing import Optional


# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归实现
class Solution:

    # 二叉树的最大深度
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0  # 根节点为None,深度为0;同样也是base_case
        # 根节点不为空,左边的最大深度和右边的最大深度,取最大的那一个,然后再加一个1(根节点)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # 二叉树的最小深度
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0  # 当前的树是空树
        if not root.left and not root.right: return 1  # 当前节点是叶节点
        # 上面两个也都是base_case,递归结束的条件
        # root既不是空,也不是叶节点
        l_deep = 100000  # 先初始化左边的最大深度为100000(最大的情况)
        r_deep = 100000  # 右边也一样
        if root.left: l_deep = self.minDepth(root.left)  # 有左节点,才去左节点去递归求最小深度
        if root.right: r_deep = self.minDepth(root.right)  # 有右节点,去右节点求最小深度
        return min(l_deep, r_deep) + 1  # 返回左边的最小深度和右边的最小深度的小的那个然后+1(root节点)
