""" 打家劫舍问题 """
# 测试链接:https://leetcode.cn/problems/house-robber-iii/
# 直接复制下面的Solution类,复制到力扣里面

from typing import Optional


# 二叉树的节点的定义  注意:提交的时候不要提这个类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    yes = 0  # 全局变量,完成了某一颗子树的遍历,返回之后,yes变成,在偷这颗子树的头节点的情况下,最大的收益
    no = 0  # 全局变量,完成了某一颗子树的遍历,返回之后,no变成,在不偷这颗子树的头节点的情况下,最大的收益

    def rob(self, root: Optional[TreeNode]) -> int:
        self.fun(root)  # 执行fun(root)
        # yes变成不偷根节点的最大收益 no变成偷头节点的最大收益
        return max(self.yes, self.no)

    # fun(cur)执行后,会把yes修改成偷cur.val的最大收益 ; 把no修改成不偷cur.val的最大收益
    def fun(self, cur: Optional[TreeNode]):
        """
        :param cur: 以cur为头节点的树
        :return: fun(cur)执行后,会把yes修改成偷cur.val的最大收益 ; 把no修改成不偷cur.val的最大收益
        """
        if not cur:  # 如果遇到空树,也就是base_case的情况
            self.yes = 0  # 偷头节点是0的收益
            self.no = 0  # 不偷头节点也是0的收益
        else:
            y = cur.val  # 局部变量y(偷头节点),先 y = 0 + cur.val加上
            n = 0  # 局部变量n(不偷头节点) n = 0

            self.fun(cur.left)  # 去左子树递归
            # yes变成偷左节点的最大收益
            # no变成不偷左节点的最大收益
            y += self.no  # 偷当前cur节点,就不能偷下一层的节点了
            n += max(self.yes, self.no)  # 不偷cur自己,可以偷下一层yes,也可以不偷下一层no

            self.fun(cur.right)  # 去右树递归
            # yes变成偷右节点的最大收益
            # no变成不偷右节点的最大收益
            y += self.no  # 偷当前cur节点,就不能偷下一层的节点了
            n += max(self.yes, self.no)  # 不偷cur自己,可以偷下一层yes,也可以不偷下一层no

            self.yes = y  # 修改全局变量,不偷当前节点的最大收益
            self.no = n  # 修改全局变量,不偷当前节点的最大收益
