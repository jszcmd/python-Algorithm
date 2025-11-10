""" 非递归实现二叉树的遍历 """


# 时间复杂度:O(n)
# 空间复杂度:O(h),h是二叉树的高度

class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


# 先序打印所有节点,非递归版
def preOrder(root: TreeNode):
    if root is not None:
        # 先把头节点压入进去
        stack = [root]
        # 如果栈里面不为空
        while stack:
            # 就先弹出这个节点,然后再打印
            root = stack.pop()
            print(root.val, end=" ")
            # 如果右边不为空,先压入右
            if root.right is not None:
                stack.append(root.right)
            # 如果左边不为空,再压入左边
            if root.left is not None:
                stack.append(root.left)
            # 这样弹出的顺序就是,先弹出左边的,在弹出右边的
        print()


# 中序打印所有节点,非递归版
# 1)来到某一个子树的头,左边界进栈,一直然它的左边界进栈,知道左边界遍历完
# 2)从栈里弹出某个节点,打印,然后重复步骤 1)
# 3)没有子树了,且栈空了
def inOrder(head: TreeNode):
    if head is not None:
        stack = []
        # 栈不为空,或者是当前的子树不为空
        while stack or head is not None:
            if head is not None:
                # 把head压入到栈里面去
                stack.append(head)
                # head节点调整到,该节点的左树
                head = head.left
            # 当head等于None的时候,栈不为空,走else
            else:
                # 栈顶弹出,弹出就打印
                head = stack.pop()
                print(head.val, end=" ")
                # head调整到弹出的这个节点的右数
                head = head.right
        print()


# 后序打印所有节点,非递归版 - 两个栈的方法
def posOrderTwoStacks(root: TreeNode):
    if root is not None:
        stack = []
        collect = []
        stack.append(root)
        while stack:
            root = stack.pop()
            # 把弹出的节点用另一个栈收集起来
            collect.append(root)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        # 从collect栈中依次打印
        while collect:
            print(collect.pop().val, end=" ")
        print()


# 后序打印所有节点,非递归版 - 一个栈的方法
def posOrderOneStack(h: TreeNode):
    if h is not None:
        # 一开始准备好一个栈,把h压进去
        stack = [h]
        # 如果始终没有打印过节点，h就一直是头节点
        # 一旦打印过节点,h就变成打印节点
        # 之后h的含义 : 上一次打印的节点
        while stack:
            cur = stack[-1]
            if cur.left is not None and h != cur.left and h != cur.right:
                # 有左树且左树没处理过
                stack.append(cur.left)
            elif cur.right is not None and h != cur.right:
                # 有右树且右树没处理过
                stack.append(cur.right)
            else:
                # 左树、右树 没有 或者 都处理过了
                print(cur.val, end=" ")
                h = stack.pop()
        print()


if __name__ == '__main__':
    # 创建上面图形所示的二叉树
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    print("用非递归实现先序遍历:")
    preOrder(head)

    print("用非递归实现中序遍历:")
    inOrder(head)

    print("用两个栈实现非递归后序遍历二叉树:")
    posOrderTwoStacks(head)

    print("用一个栈实现非递归后序遍历二叉树:")
    posOrderTwoStacks(head)
