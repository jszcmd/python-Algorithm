class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归基本样子,用来理解递归序
def f(head):
    if head is None: return

    print(head.val, end=" ")
    # 1 第一次来到head的位置

    f(head.left)
    print(head.val, end=" ")
    # 2 第二次来到head位置

    f(head.right)
    print(head.val, end=" ")
    # 第三次来到head的位置

    # 每一个节点都会来到3次


# 先序打印所有节点,递归版
# 时间复杂度: O(n)
# 空间复杂度: O(h) (h为二叉树的高度)
def preOrder(head):
    if head is None: return
    # 先打印
    print(head.val, end=" ")
    # 再去左树
    preOrder(head.left)
    # 再去右树
    preOrder(head.right)


# 中序打印所有节点,递归版
# 时间复杂度: O(n)
# 空间复杂度: O(h) (h为二叉树的高度)
def inOrder(head):
    # 如果是None就返回
    if head is None:
        return
    # 先去左树
    inOrder(head.left)
    # 回去之后,打印
    print(head.val, end=" ")
    # 再去右树
    inOrder(head.right)
    # 结束


# 后序打印所有节点,递归版
# 时间复杂度: O(n)
# 空间复杂度: O(h) (h为二叉树的高度)
def posOrder(head):
    if head is None:
        return
    # 先去左树
    posOrder(head.left)
    # 再去右树
    posOrder(head.right)
    # 再打印
    print(head.val, end=" ")


def main():
    # 创建上面图形所示的二叉树
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    # 递归序
    print("递归序,每一次访问都打印:")
    f(head)
    print()
    print()

    print("用递归实现先序遍历(先序,每一次访问才打印):")
    preOrder(head)
    print()
    print()

    print("用递归实现中序遍历(中序,第二次访问才打印):")
    inOrder(head)
    print()
    print()

    print("用递归实现后序遍历(后序,第三次访问才打印):")
    posOrder(head)


if __name__ == "__main__":
    main()
