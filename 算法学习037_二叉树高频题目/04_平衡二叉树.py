""" 平衡二叉树 """
# 力扣测试链接:https://leetcode.cn/problems/balanced-binary-tree/
# 直接把Solution复制到力扣里面就可以了
from typing import Optional


# 二叉树节点的定义,注意不要提交这个类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 平衡二叉树:每一个节点左树的高度和右树的高度相差不超过1
class Solution:
    is_balance = True  # 设置一个全局变量,默认是二叉树

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balance = True  # 每一次测试,都设置为True
        self.height(root)
        return self.is_balance

    # 当前以cur为根节点的子树,求这个树的高度
    # 一旦发现不平衡的点,把is_balance改成False,返回什么高度已经不重要了
    def height(self, cur: Optional[TreeNode]) -> int:
        # 一旦发现不平衡,返回什么高度已经不重要了,我们就直接返回0
        if not self.is_balance or not cur: return 0
        lh = self.height(cur.left)  # 去递归求左侧的高度
        rh = self.height(cur.right)  # 去递归求右侧的高度
        if abs(lh - rh) > 1: self.is_balance = False  # 发现不平衡的点
        return max(lh, rh) + 1  # 一切正常,返回正常的高度
