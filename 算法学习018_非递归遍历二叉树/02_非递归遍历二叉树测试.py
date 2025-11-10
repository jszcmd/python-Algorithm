""" 非递归遍历二叉树:前序,中序和后序 """
# 前序遍历二叉树:
#   测试链接:https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
# 中序遍历二叉树:
#   测试链接:https://leetcode.cn/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=binary-tree
# 后序遍历二叉树:
#   测试链接:https://leetcode.cn/problems/binary-tree-postorder-traversal/

# 时间复杂度:O(n)


from typing import Optional, List


# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 先序遍历:使用一个栈实现二叉树的先序遍历
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        先序遍历:使用一个栈实现二叉树的先序遍历
        :type root: TreeNode
        :param root: 二叉树节点的根节点
        :return: 返回先序收集到数组
        """
        ans = []  # 准备一个存储节点val的数组
        if not root: return ans  # 如果根节点为空,返回空数组
        # root不为空的情况
        nodes = [root]  # 申请一个栈,先把头节点压进去
        # 栈不为空,弹出一个栈顶,先压右再压左边
        while nodes:  # 栈不为空
            head = nodes.pop()
            ans.append(head.val)  # 把弹出的节点的val压入到ans
            # 先压入右树
            if head.right: nodes.append(head.right)
            # 再压入左树
            if head.left: nodes.append(head.left)
        return ans

    # 中序遍历
    def inorderTraversal(self, head: Optional[TreeNode]) -> List[int]:
        """
        :param head: 第一次传入的head为二叉树的根节点,后面会改变
        :return:
        (1):二叉树左边界进栈
        (2):弹出节点,打印(压入到ans),弹出节点的右树重复步骤(1)
        (3):一直到没有子树并且栈为空,结束
        """
        ans = []  # 准备一个存储节点val的数组
        if not head: return ans  # 如果根节点为空,返回空数组
        # root不为空的情况
        nodes = []
        while nodes or head:
            if head:  # head不为空
                nodes.append(head)  # 把head加入到栈里面去
                head = head.left  # head左移
            else:
                head = nodes.pop()
                ans.append(head.val)  # 收集节点
                head = head.right  # head跑到右树上
        return ans

    # 一个栈实现后续遍历
    def postorderTraversal(self, h: Optional[TreeNode]) -> List[int]:
        """
        :type h: TreeNode
        :param h: 传入的h是二叉树的根节点,root;下面的h会改变
        :return: 返回后序收集到数组
        """
        ans = []  # 准备一个存储节点val的数组
        if not h: return ans  # 如果根节点为空,返回空数组
        # root不为空的情况
        nodes = [h]  # 申请一个栈,先把头节点压进去
        # 如果始终没有打印过节点,h就一直是头节点
        # 一旦打印过节点,h就变成了打印节点
        # 之后h的含义:上一次打印的节点
        while nodes:  # 栈里面有元素
            cur = nodes[-1]  # 取到栈顶元素,不弹出
            # 分支(1):有左树,h既不等于左树,也不等于右树
            if cur.left and h != cur.left and h != cur.right:
                nodes.append(cur.left)  # 有左树,且左树没有处理过
            # 分支(2):有右孩子,h不等于右孩子
            elif cur.right and h != cur.right:
                nodes.append(cur.right)  # 有右树,且右树没有处理过
            else:  # 左树,右树都没有或者都处理过了
                ans.append(cur.val)
                h = nodes.pop()
        return ans

    # 后序遍历(用两个栈实现),如果想测试这个,把函数名后面的2去掉
    # 先序: 中 左 右  ---> 得到: 中 右 左 ---> 倒过来得到: 左 右 中
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: TreeNode
        :param root: 二叉树节点的根节点
        :return: 返回后序收集到数组
        """
        ans = []  # 准备一个存储节点val的数组(同时模拟一个栈)
        if not root: return ans  # 如果根节点为空,返回空数组
        # root不为空的情况
        nodes = [root]  # 申请一个栈,先把头节点压进去
        # 栈不为空,弹出一个栈顶,先压右再压左边
        while nodes:  # 栈不为空
            head = nodes.pop()
            ans.append(head.val)  # 把弹出的节点的val压入到ans
            # 再压入左树
            if head.left: nodes.append(head.left)
            # 先压入右树
            if head.right: nodes.append(head.right)
        # 上面我们收集的是: 中 右 左
        ans.reverse()  # 反转一下:中 左 右
        return ans
