""" 判断是不是完全二叉树 """
# 测试链接:https://leetcode.cn/problems/check-completeness-of-a-binary-tree/

from typing import Optional


# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 规则(1):如果有右节点,但是没有左节点,不是完全二叉树;返回False
    # 规格(2):一旦发现孩子不全的节点(叶节点,有左节点无右节点),接下来必须全是叶节点,否则不是完全二叉树
    node_queue = [None] * 101  # 准备一个队列,用于层序有限遍历

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 空节点也是完全二叉树
        if not root: return True
        l = 0  # 队头初始化
        r = 0  # 队尾初始化
        self.node_queue[r] = root  # 根节点加入队列
        r += 1  # 更新队尾
        have_leaf = False  # 是否遇到过左右两个孩子不全的节点
        while l < r:  # 队列里面有东西
            cur = self.node_queue[l]  # 拿出队头的元素
            l += 1  # 更新队头
            # 第一个违规条件,有右孩子,但是没有左孩子
            if not cur.left and cur.right: return False
            # 第二个违规条件:如果遇到过孩子不全的节点,并且当前cur节点还不是叶节点
            if have_leaf and (cur.left or cur.right): return False
            if cur.left:  # 有左节点加入左节点
                self.node_queue[r] = cur.left
                r += 1
            if cur.right:  # 有右节点,加入右节点
                self.node_queue[r] = cur.right
                r += 1
            # 左孩子或者右孩子为空,那么就遇到左右孩子不全的节点
            if not cur.left or not cur.right: have_leaf = True
        return True
