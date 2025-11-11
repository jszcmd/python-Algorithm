""" 链表实现双端队列 """
# 测试链接:https://leetcode.cn/problems/design-circular-deque/

""" (1):使用python内置的deque实现 """
# collections.deque 是用块状数组+双向链表的混合结构
# 注意:提交的时候把类名改成MyCircularDeque,python内置的deque实现的更快
from collections import deque


# 内置的deque实现的双端队列
class MyCircularDeque1:
    def __init__(self, k: int):
        self.limit = k  # 设置队列的最大长度
        self.items = deque(maxlen=k)  # 创建python内置的双端队列的对象

    # 向队列的头部插入一个元素
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.items.appendleft(value)
            return True

    # 向队列的尾部添加一个元素
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.items.append(value)
            return True

    # 删除队列头部的元素
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.items.popleft()
            return True

    # 删除队尾的元素
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.items.pop()
            return True

    # 获取队头的元素,不弹出
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.items[0]

    # 获取队尾的元素
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.items[-1]

    # 判断队列是否为空
    def isEmpty(self) -> bool:
        return len(self.items) == 0

    # 判断队列是否满了
    def isFull(self) -> bool:
        return len(self.items) == self.limit


""" (2):手搓双向链表实现双端队列: """


# 双向链表的定义
class ListNode:
    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class MyCircularDeque:
    # 初始化
    def __init__(self, k: int):
        self.limit = k  # 初始化队列的最大长度
        self.head = ListNode(-1)  # 初始化头节点,头节点的下一个节点储存的才是真正的第一个元素的节点
        self.tail = self.head  # 初始化tail==head,表示队列为空
        self.size = 0  # 队列的长度初始化为0

    # 向队列的头部添加一个元素
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False  # 队列满了,不能添加元素
        else:  # 队列没有满
            new_node = ListNode(value)  # 先创建一个新节点
            if self.isEmpty():  # (1):单独处理队列为空的情况
                # 队列为空,加入一个元素后的队列: head(头节点)  ---  tail(也是new_node)
                self.head.next = new_node  # 处理后继: head --(next)--> new_node
                self.tail = new_node  # tail指向新加入的节点
                new_node.pre = self.head  # 处理前驱: tail(也是new_node) --(pre)--> head(头节点)
            else:  # 队列里面的元素不为空
                p = self.head.next  # 先记录下存储队列中的第一个有效元素的节点
                # 处理后继关系:head --(next)--> ListNode(value) --(next)--> p
                self.head.next = new_node
                new_node.next = p
                # 处理前驱关系:p(原本的队头) --(pre)--> ListNode(value) --(pre)--> head
                p.pre = new_node
                new_node.pre = self.head
            self.size += 1  # 队列的长度+1
            return True

    # 向队列的队尾添加一个元素
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False  # 队列满了,不能添加元素
        else:  # 队列没有满
            new_node = ListNode(value)  # 先创建一个新节点
            if self.isEmpty():  # (1):处理队列为空的情况
                # 队列为空,加入一个元素后的队列: head(头节点)  ---  tail(也是new_node)
                self.head.next = new_node  # 处理后继: head --(next)--> new_node
                self.tail = new_node  # tail指向新加入的节点
                new_node.pre = self.head  # 处理前驱: tail(也是new_node) --(pre)--> head(头节点)
            else:  # (2):队列里面的元素不为空
                # 处理后继: tail --(next)--> new_node
                self.tail.next = new_node
                # 处理前驱: new_node --(pre)--> tail
                new_node.pre = self.tail
                self.tail = new_node  # 更新队尾tail
            self.size += 1  # 队列的长度+1
            return True

    # 删除队列头部的元素
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False  # 队列为空,不能删除
        else:  # 队列不为空
            if self.size == 1:  # (1):队列只有一个元素,删除后变为空队列
                self.head.next = None  # head的后继指向None
                self.tail = self.head  # tail指向head
            else:  # (2):队列中的元素不止一个
                p = self.head.next  # 要删除的节点
                self.head.next = p.next  # head指向新的头节点
                p.next.pre = self.head  # 新的头节点指向head;(p.next)就变成了第一个有效的节点
            self.size -= 1  # 队列的长度-1
            return True

    # 删除队尾的元素
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.size == 1:  # (1):队列只有一个元素,删除后变为空队列
                self.head.next = None  # head的后继指向None
                self.tail = self.head  # tail指向head
            else:  # (2):队列中的元素不止一个
                new_tail = self.tail.pre  # 标记队尾的前一个节点
                new_tail.next = None  # 标记的节点的后继指向None
                self.tail = new_tail  # 更新队尾tail
            self.size -= 1  # 队列的长度-1
            return True

    # 获取队列头部的元素,不弹出
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val  # (head.next)才是真正存储第一个元素的节点

    # 获取队列尾部的元素,不弹出
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.val  # tail就是队尾元素的节点

    # 判断队列是否为空
    def isEmpty(self) -> bool:
        return self.size == 0

    # 判断队列是否满
    def isFull(self) -> bool:
        return self.size == self.limit
