""" 从前序与中序遍历序列构造二叉树 """
# 已知:先序和中序遍历的结果(无重复值),把这棵二叉树建出来
# 如果有重复值的情况下,这棵树可能不唯一
# 测试链接:https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


# 已知:先序和中序遍历的结果(无重复值),把这棵二叉树建出来
# 如果有重复值的情况下,这棵树可能不唯一

# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 遍历inorder数组里面的内容,把数组对应索引的值当作key,对应索引当作value
        hashmap = {value: i for i, value in enumerate(inorder)}
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, hashmap)  # 递归建树

    # 拿pre_arr[l1]位置建立头节点,建树的函数,返回建立的头节点
    def build(self, pre_arr: List[int], l1: int, r1: int, in_arr: List[int], l2: int, r2: int, hashmap: dict) -> \
            Optional[TreeNode]:
        if l1 > r1: return None  # 如果l1>r1,直接返回None
        head = TreeNode(pre_arr[l1])  # 头节点一定是pre_arr[l1]位置
        if l1 == r1: return head  # 如果只有一个节点,把头结点建好就返回
        k = hashmap[pre_arr[l1]]  # 找到头节点在in_arr数组中什么位置
        # l1 l1+1 .....    r1           头节点I(l1) 头节点的左树 头节点的右树
        # l2 l1+1 ..... k  k+1 ..... r2 头节点的左树 头节点(k) 头节点的右树
        # 前k-l2个都是head的左树  继续递归,用pre_arr中的[l1+1,l1+k-l2](一共k-l2)和in_arr中的[l2,k-1]继续去左边递归建树
        # 后面的k到r2的都是head的右树,用pre_arr中的[l1+k-l2+1,r2]和in_arr中的[k+1,r2]去递归建立右树
        head.left = self.build(pre_arr, l1 + 1, l1 + k - l2, in_arr, l2, k - 1, hashmap)
        head.right = self.build(pre_arr, l1 + k - l2 + 1, r1, in_arr, k + 1, r2, hashmap)
        return head
