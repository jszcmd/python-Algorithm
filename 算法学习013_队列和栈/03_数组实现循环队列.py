# 测试链接:https://leetcode.cn/problems/design-circular-queue/
# 直接把下面的MyCircularQueue类复制到力扣里就可以运行了;
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k  # 初始化一个数组,长度为k
        self.head = 0  # 初始化队列的头部为0
        self.tail = 0  # tail为队列尾部的索引值超前1
        self.size = 0  # 初始化队列的长度为0
        self.limit = k  # 队列最多可以容纳k个元素

    # 向队列尾部加入一个元素,添加成功返回True,失败返回False
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False  # 队列满了,不能添加元素
        self.arr[self.tail] = value  # 直接把value加入到索引为tail的位置
        self.tail = 0 if (self.tail == self.limit - 1) else self.tail + 1  # 更新tail位置
        self.size += 1  # 队列的长度加1
        return True

    # 向队列的头部删除一个元素,删除成功返回True,失败返回False
    def deQueue(self) -> bool:
        if self.isEmpty(): return False  # 队列为空,不能够删除元素
        self.head = 0 if (self.head == self.limit - 1) else self.head + 1  # 更新tail的位置
        self.size -= 1  # 队列的长度-1
        return True

    # 获取队头的元素
    def Front(self) -> int:
        if self.isEmpty(): return -1  # 队列为空,返回-1
        return self.arr[self.head]  # 有元素,直接返回索引为head位置的元素;

    # 获取队尾的元素;
    def Rear(self) -> int:
        if self.isEmpty(): return -1  # 队列为空,返回-1
        last = self.limit - 1 if (self.tail == 0) else self.tail - 1  # last确定队列尾部的索引值
        return self.arr[last]  # 返回索引值为last位置的元素;
        # 也可以直接返回self.arr[self.tail-1];python中arr[-1]为数组最后一个元素;

    # 队列是否为空
    def isEmpty(self) -> bool:
        return self.size == 0  # 队列的长度为0,那么就是空了

    # 队列是否满了
    def isFull(self) -> bool:
        return self.size == self.limit  # 队列的长度为最大限度,队列满了;

# 你的MyCircularQueue对象将被实例化,并按照以下方式调用:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
