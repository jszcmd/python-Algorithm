""" 搜索二叉树的最近公共祖先 """


# 测试链接:https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 提交的时候不要提交下面的TreeNode类

# 二叉树节点的定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 从root开始从上往下开始
        # 如果先遇到p,说明p是答案
        # 如果先遇到q,说明q是答案
        # 如果root在p~q之间,不管p和q谁大谁小,只要是root在中间,那么此时的root就是答案
        # 如果root在p~q的左侧,那么root往右移动
        # 如果root在p~q的右侧,那么root往左移动
        while root.val != p.val and root.val != q.val:
            # 如果root在p~q之间,不管p和q谁大谁小,只要是root在中间,那么此时的root就是答案
            if min(p.val, q.val) < root.val < max(p.val, q.val): break
            # 如果root在p~q的左侧,那么root往右移动
            # 如果root在p~q的右侧,那么root往左移动
            root = root.right if root.val < min(p.val, q.val) else root.left
        return root
