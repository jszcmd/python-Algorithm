""" 修剪二叉搜索树 """
# 测试链接:https://leetcode.cn/problems/trim-a-binary-search-tree/
# 直接把下面的Solution类复制到力扣里面

from typing import Optional


# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 只留下[low,high]左闭右闭的范围的值保留
    def trimBST(self, cur: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not cur: return None  # 当前是空节点,往上返回空,保留空节点
        # 当cur节点的值小于low,那么cur左树,连同cur都不用看了,一定是不保留的
        if cur.val < low: return self.trimBST(cur.right, low, high)  # 去右树看看
        # 当cur当前节点的值大于high,那么cur的右数,连同cur都不用看了,一定是不保留的
        if cur.val > high: return self.trimBST(cur.left, low, high)  # 去左树看看
        # cur在范围[low,high]的时候,cur一定可以保留的
        cur.left = self.trimBST(cur.left, low, high)  # cur左边连上左边修剪好的
        cur.right = self.trimBST(cur.right, low, high)  # cur右边连上右边修剪好的
        return cur
