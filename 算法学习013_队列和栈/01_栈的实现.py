""" (1):用列表来实现栈 """

# (a):初始化一个空的数组栈
arr_stack = []

# (b):向栈顶加入一个元素:
arr_stack.append(1)
arr_stack.append(2)
arr_stack.append(3)

# (c):弹出栈顶的元素 pop(),默认弹出数组中最后一个元素
# pop()函数的返回值为弹出的元素
print(arr_stack.pop())

# (d):获取栈顶的元素,但是不弹出
print(arr_stack[-1])

# (e):判断栈是否为空
print(len(arr_stack) == 0)

# (f):判断栈是否满了
# print(len(arr_stack) == MAXSIZE)

""" 当然,用上面这种方法是时最简单的但是封装性不是太好,如果非常大的数据量的话,append实现时很耗时间的 """

""" (2):用数组实现的封装起来的栈 """


# 用数组实现的栈
class ArrStack:
    # 对栈进行初始化,形参k是栈的最大长度
    def __init__(self, k):
        self.stack = [-1] * k  # 初始化一个长度为k的栈
        self.limit = k  # 初始化栈的最大长度限制为k
        self.size = 0  # 初始化长度为0,同时size表示栈中已有元素的下一个位置

    # 向栈顶加入一个元素value,加入成功返回True,否则返回False
    def push(self, value):
        if self.isFull(): return False  # 栈满了,不能添加元素
        self.stack[self.size] = value  # 在索引为size的位置添加value
        self.size += 1  # 长度+1
        return True

    # 删除栈顶的元素,删除成功返回True,失败返回False
    def pop(self):
        if self.isEmpty(): return False  # 栈为空,不能删除
        self.size -= 1  # 直接调整size的位置就可以了
        return True  # 只返回操作成功与否，不返回元素值

    # 取出栈顶的元素,不弹出
    def top(self):
        if self.isEmpty(): return -1  # 空栈时返回-1或其他默认值
        return self.stack[self.size - 1]  # 返回索引为size-1位置的元素

    # 获取栈中的元素个数
    def length(self):
        return self.size

    # 判断栈是否为空
    def isEmpty(self):
        return self.size == 0

    # 判断栈是否满
    def isFull(self):
        return self.size == self.limit


""" (3):用链表实现栈 """


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class LinkStack:
    # 初始化栈
    def __init__(self, k):
        self.head = None  # 开始head指向None
        self.limit = k  # 栈最多可以容纳k个元素
        self.size = 0  # 初始化栈的长度为0

    # push(value):在链表头部插入新节点,插入成功返回True,失败返回False
    def push(self, value):
        if self.isFull(): return False  # 栈满了,不能插入;
        p = ListNode(value)  # 创建新的节点
        p.next = self.head  # 新节点的next指向头节点
        self.head = p  # 更新头节点为新节点
        self.size += 1  # 长度+1
        return True

    # pop(): 删除栈顶元素,删除成功返回True,失败返回False
    def pop(self):
        if self.isEmpty(): return False  # 栈为空,不能删除元素
        p = self.head  # 记录当前栈顶的节点
        self.head = p.next  # 修改head指向新的头节点
        self.size -= 1  # 长度-1
        p.next = None  # 把删除的节点指向None;
        return True

    # 返回栈顶的元素,不弹出;成功返回弹出的值,失败返回-1
    def top(self):
        if self.isEmpty(): return -1
        return self.head.val  # 返回头节点head的val的值

    # 判断栈是否为空
    def isEmpty(self):
        return self.size == 0

        # 判断栈是否满

    def isFull(self):
        return self.size == self.limit

    # 获取当前栈中的元素;
    def length(self):
        return self.size
