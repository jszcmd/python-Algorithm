""" 普通二叉树的最近公共祖先 """


# 测试链接:https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# 提交的时候不要提交下面的TreeNode类

# 二叉树节点的定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 关系1:彼此包含
    # 关系2:分了两树
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 遇到空,或者p或者q直接返回
        if not root or root == p or root == q: return root
        # 去左树搜索p和q,遇到空,或者p或者q直接返回
        l = self.lowestCommonAncestor(root.left, p, q)
        # 右树搜索p和q,遇到空,或者p或者q直接返回
        r = self.lowestCommonAncestor(root.right, p, q)
        # 左树1也搜到,右树也搜到,就返回此时的root
        if l and r: return root
        # 都没有搜到,返回空
        if not l and not r: return None
        # 到这里就是一个为空,一个不为空,返回不空的那一个
        return l if l else r
