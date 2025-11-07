""" 路径总和 """
# 测试链接:https://leetcode.cn/problems/path-sum-ii/description/
# 直接把下面的Solution类复制到力扣里面就可以了

from typing import Optional, List


# 二叉树节点的定义  ######## 注意,不要提交这个类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []  # 如果root为空,直接返回
        if root:  # 如果根节点不为空
            path = []  # 准备一个记录走过路径的列表
            self.process(root, targetSum, 0, path, ans)
        return ans

        # 递归调用

    def process(self, cur: Optional[TreeNode], targetSum: int, sum_: int, path: List[int], ans):
        """
        :param cur: 代表当前来到cur节点的位置
        :param targetSum: 目标累加和
        :param sum_: 来到cur位置,不包括cur自己,cur上方经过节点,上方一整条路径的累加和
        :param path: 走过的路径列表
        :param ans: 要返回的结果,ans是一个嵌套列表
        :return: 这个函数直接再ans里面操作不需要返回值
        """
        # 当前节点cur为叶节点的时候
        if not cur.left and not cur.right:
            if cur.val + sum_ == targetSum:
                ans.append(path[:] + [cur.val])
            return  # 隐式返回，递归到此结束
        else:  # 当前节点不是叶节点
            path.append(cur.val)  # 把当前节点加入到走过的路径之中
            # 去cur的左孩子递归调用,当左孩子结束的时候,也会弹出左孩子自己的val
            if cur.left: self.process(cur.left, targetSum, sum_ + cur.val, path, ans)
            # 去cur的右孩子递归调用,当右孩子结束的时候,也会弹出右孩子自己的val
            if cur.right: self.process(cur.right, targetSum, sum_ + cur.val, path, ans)
            path.pop()  # 恢复原状,再把cur.val弹出
            # 如果到这里所有的子递归都处理完了,也就结束了

    def process2(self, cur: Optional[TreeNode], targetSum: int, sum_: int, path: List[int], ans):
        """
        :param cur: 代表当前来到cur节点的位置
        :param targetSum: 目标累加和
        :param sum_: 来到cur位置,不包括cur自己,cur上方经过节点,上方一整条路径的累加和
        :param path: 走过的路径列表
        :param ans: 要返回的结果,ans是一个嵌套列表
        :return: 这个函数直接再ans里面操作不需要返回值
        """
        # 当前节点cur为叶节点的时候
        if not cur.left and not cur.right:
            if cur.val + sum_ == targetSum:  # 如果走到叶节点了,发现达到目标值了
                path.append(cur.val)  # 把叶节点的值加入到走的路径之中
                copy_path = path[:]  # 把这条路径拷贝一份
                # 还可以使用:path.copy()拷贝一份;list(path)再创建一份新的一模一样的
                # ######## 注意: copy_path = path 这个只是拷贝了一份引用,修改copy_path就是修改path中的值
                ans.append(copy_path)  # 把这次的路径加入到ans里面
                path.pop()  # 处理之后,恢复原状
            return  # 隐式返回，递归到此结束
        else:  # 当前节点不是叶节点
            path.append(cur.val)  # 把当前节点加入到走过的路径之中
            # 去cur的左孩子递归调用,当左孩子结束的时候,也会弹出左孩子自己的val
            if cur.left: self.process2(cur.left, targetSum, sum_ + cur.val, path, ans)
            # 去cur的右孩子递归调用,当右孩子结束的时候,也会弹出右孩子自己的val
            if cur.right: self.process2(cur.right, targetSum, sum_ + cur.val, path, ans)
            path.pop()  # 恢复原状,再把cur.val弹出
            # 如果到这里所有的子递归都处理完了,也就结束了
