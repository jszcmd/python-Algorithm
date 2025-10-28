"""
队列:先进先出
添加元素在队列的尾部进行;删除元素在队列的头部进行.
"""

"""(1):使用python内部实现的普通的队列"""
# 注意:用这个来实现队列不能够实现:
#     获取队列尾部的元素,不弹出
#     获取队列头部的元素,不弹出
import queue

# 初始化队,maxsize设置队列最多的元素
q = queue.Queue(maxsize=3)

# 向队列尾部添加一个元素;
q.put('A')
q.put('B')
q.put('C')

# 从队列头部弹出元素出队
print(q.get())  # 'A'
print(q.get())  # 'B'

# 判断队列是否为空
print(q.empty())
# 判断队列是否满了
print(q.full())
# 判断队列的长度
print(q.qsize())

"""(2):使用链表来实现普通的队列:"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class LinkQueue:
    def __init__(self, k: int):
        self.limit = k  # 队列可容纳最多k个元素
        # 初始化一个头节点,这个头节点指向的下一个节点中存储的才是真正有效的队列队头的元素
        self.head = ListNode(-1)  # head为队列队列的前一个,类似与哨兵节点
        self.tail = self.head  # 初始时:tail和head指向相同,说明队列为空
        self.size = 0  # 初始队列的长度为0

    # 向队列的尾部添加一个元素value,添加成功返回True,否则返回False;
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False  # 队列满了,不能添加元素
        self.tail.next = ListNode(value)  # tail指向新建的节点
        self.tail = self.tail.next  # 更新tail
        self.size += 1  # 队列的长度+1
        return True

    # 向队列的队头删除,删除成功返回True,否则返回False;
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        # 记录head的下一个节点,head.next才是真实存储队列头部元素的节点
        p = self.head.next  # 记录head的下一个节点,head.next才是真实存储队列头部元素的节点
        self.head.next = p.next  # 调整head节点的下一个节点为,p的下一个节点;
        if self.tail == p:  # 如果发现,p等于队列尾部的节点,那么说明原来队列就一个元素;
            self.tail = self.head  # 再把tail和head指向同一个,说明此时队列又为空了;
        self.size -= 1  # 队列的长度-1
        p.next = None  # 显式断开引用,帮助垃圾回收
        return True

    # 获取队列头部的元素,不弹出;获取失败返回-1(假设我们的操作数没有-1)
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.val

    # 获取队列队尾的元素,不弹出;获取失败返回-1(假设我们的操作数没有-1)
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.val

    # 判断队列是否为空
    def isEmpty(self) -> bool:
        return self.size == 0  # 队列的长度为0,则为空

    # 判断队列是否满了
    def isFull(self) -> bool:
        return self.size == self.limit  # 队列的长度为k,则满了

    # 获取队列的长度
    def length(self) -> int:
        return self.size


""" (3): 用数组实现队列"""
# 用数组实现循环队列:参考下面的03_数组循环队列;
