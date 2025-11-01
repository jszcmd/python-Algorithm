""" 二叉树最大宽度 """
from typing import Optional


# 测试链接:https://leetcode.cn/problems/maximum-width-of-binary-tree/

# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        node_queue = [None] * 3001  # 节点队列
        id_queue = [-1] * 3001  # 编号队列
        l = 0
        r = 0  # 对两个队列初始化
        ans = 1  # ans我们要返回的答案,默认是1,有root的情况
        node_queue[r] = root  # 把根节点加入到节点队列
        id_queue[r] = 1  # root节点的编号是1
        r += 1  # 更新队尾
        while l < r:  # 队列里面还有东西,就继续遍历
            size = r - l  #
            # 现在队列的最左在l位置,队列的最右在r-1位置
            # 当前层有几个节点:id_queue[r-1]-id_queue[r] ;然后与ans比较哪个大
            ans = max(ans, id_queue[r - 1] - id_queue[l] + 1)
            for i in range(size):
                cur = node_queue[l]  # 弹出节点
                num = id_queue[l]  # 弹出id
                l += 1  # 跟新队头索引
                if cur.left:  # 有左节点
                    node_queue[r] = cur.left  # 左节点入节点队列
                    id_queue[r] = num * 2  # cur左节点的编号是cur编号的2倍
                    r += 1  # 更新队尾
                if cur.right:  # 有右节点
                    node_queue[r] = cur.right  # 右节点入队
                    id_queue[r] = num * 2 + 1  # cur右节点的编号是cur编号的2倍+1
                    r += 1  # 更新队尾
        return ans
