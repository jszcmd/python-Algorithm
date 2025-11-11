""" 设计实现双端队列 """
# 测试链接:https://leetcode.cn/problems/design-circular-deque/
# 直接把下面的MyCircularDeque类复制到力扣里面

from typing import List


class MyCircularDeque:

    # 初始化双端队列
    def __init__(self, k: int):
        self.l: int = 0  # 初始化队头索引为0
        self.r: int = 0  # 初始化队尾索引为0
        self.size: int = 0  # 初始化队列的长度为0
        self.limit = k  # 队列的最大长度为k
        self.arr: List[int] = [-1] * k  # 用一个长度为k的数组模拟双端队列

    # 向队列头部加入一个元素
    def insertFront(self, value: int) -> bool:
        """
        :param value: 要添加到队列头部的元素
        :return: 插入成功返回True;否则返回False
        """
        if self.isFull():
            return False  # 队列满了,不能插入元素
        else:
            if self.isEmpty():  # 队列还是空的
                self.l = self.r = 0  # 队头和队尾都是0
                self.arr[0] = value  # 把value插入到0位置
            else:  # 队列既没有满,也不为空
                self.l = self.limit - 1 if self.l == 0 else self.l - 1
                self.arr[self.l] = value
                # (1):如果l==0,把value插入到arr[k-1]位置,l移动到k-1位置
                # (2):如果l!=0,把value插入到arr[l-1]位置,l移动到l-1位置
            self.size += 1  # 队列的长度+1
            return True

    # 向队列的队尾插入一个元素
    def insertLast(self, value: int) -> bool:
        """
        :param value: 要添加到队列尾部的元素
        :return: 插入成功返回True;否则返回False
        """
        if self.isFull():
            return False  # 队列满了,不能插入元素
        else:
            if self.isEmpty():  # 队列为空
                self.l = self.r = 0  # 队头和队尾都是0
                self.arr[0] = value  # 把value插入到0位置
            else:  # 队列既没有满,也不为空
                self.r = 0 if self.r == self.limit - 1 else self.r + 1
                self.arr[self.r] = value
                # (1):如果r==k-1,把value插入到arr[0]位置,r移动到0位置
                # (2):如果r!=k-1,把value插入到arr[r+1]位置,r移动到r+1位置
            self.size += 1  # 队列的长度+1
            return True

    # 删除队列头部的元素
    def deleteFront(self) -> bool:
        """
        删除队列头部的元素
        :return: 删除成功返回True;否则返回False
        """
        if self.isEmpty():
            return False  # 队列为空,没有元素可以删除
        else:  # 队列里面有值
            self.l = 0 if self.l == self.limit - 1 else self.l + 1
            # (1):如果l==k-1,l移动到0位置,就是实现删除队头的元素了
            # (2):如果l!=k-1,l移动到l+1位置
            self.size -= 1  # 队列的长度-1
            return True

    # 删除队尾的元素
    def deleteLast(self) -> bool:
        """
        删除队尾的元素
        :return: 删除成功返回True;否则返回False
        """
        if self.isEmpty():
            return False  # 队列为空,没有元素可以删除
        else:  # 队列里面有值
            self.r = self.limit - 1 if self.r == 0 else self.r - 1
            # (1):如果r==0,r来到k-1位置,就实现删除队列头部的元素了
            # (2):如果r!=0,r来到r-1的位置
            self.size -= 1  # 队列的长度-1
            return True

    # 得到队列头部的元素,不弹出
    def getFront(self) -> int:
        """
        得到队列头部的元素,不弹出
        :return: 有队头,返回得到的值;否则返回-1
        """
        if self.isEmpty():
            return -1  # 队列为空,返回-1
        else:
            return self.arr[self.l]  # 直接取arr[l]

    # 得到队列尾部的元素,不弹出
    def getRear(self) -> int:
        """
        得到队列尾部的元素,不弹出
        :return: 有队尾,返回得到的值;否则返回-1
        """
        if self.isEmpty():
            return -1  # 队列为空,返回-1
        else:
            return self.arr[self.r]  # 直接取arr[r]

    # 判断队列是否为空
    def isEmpty(self) -> bool:
        return self.size == 0

    # 判断队列是否满了
    def isFull(self) -> bool:
        return self.size == self.limit
