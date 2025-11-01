""" 完全二叉树的节点个数 """
# 已知一个二叉树是完全二叉树,求节点个数,要求时间复杂度小于O(n)
# 测试链接:https://leetcode.cn/problems/count-complete-tree-nodes/description/

from typing import Optional


# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 时间复杂度:o((log n)^2)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 # 整棵树是空树,返回0个节点
        # h整棵树的高度:self.left_height(root,1)
        return self.count(root,1,self.left_height(root,1))

    # 求cur这颗子树上有多少节点
    def count(self,cur,level,h):
        """
        # cur:当前来到的节点
        # level:当前来到的节点在第几层
        # h:是整棵树的高度,不是cur这颗子树的高度
        """
        if level == h: return 1 # level在最后一层cur就是叶节点
        # cur的右树上的最左节点,扎到了最深层,右树是完全二叉树h-level
        if self.left_height(cur.right,level+1) == h:
            # cur左树的所有节点+cur的结果:(1<<(h-level)),2的(h-level)次方,注意加上外围括号
            # self.count(cur.right,level+1)cur右树上算有几个节点
            return (1<<(h-level)) + self.count(cur.right,level+1,h) #
        else: # cur的右树节点没有扎到最深层,右数就是完全二叉树,高度是h-level-1
            # cur右树的所有节点+cur的结果:(1<<(h-level-1)),注意加上外围括号
            # self.count(cur.left,level+1)cur左数上面算有几个节点
            return (1<<(h-level-1)) + self.count(cur.left,level+1,h)

    # 当前节点是cur,并且它在level层
    # 返回从cur开始不停往左,能够扎到几层
    def left_height(self,cur,level):
        while cur: # 遇到None结束循环
            level += 1
            cur=cur.left
        return level -1
