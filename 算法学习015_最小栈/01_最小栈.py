""" 最小栈:填函数风格 """
# 测试链接:https://leetcode.cn/problems/min-stack/

""" (1):使用动态数组(pop,append)实现 """


# 直接把下面的代码类名改成MinStack复制到力扣里面;
# 因为append和pop的操作,当数据量很大的时候,时间就不会太好

class MinStack1:

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data.append(val)  # 数据栈直接压入数据
        # 最小栈的压入,直接压入当前数据有两种情况:
        # (1)如果最小栈为空;(2)或者是当前元素比min栈的栈顶元素还小,直接压入当前数字
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:  # 最小栈不是空的,当前数字大于min栈的栈顶,重复压入min栈的栈顶
            self.min_stack.append(self.min_stack[-1])

    # 最小栈和数据栈同时弹出栈顶元素
    def pop(self) -> None:
        self.data.pop()
        self.min_stack.pop()

    # 取出栈顶元素,不弹出,注意:这里要取data栈!!!
    def top(self) -> int:
        return self.data[-1]

    # 获取此时栈中最小的元素,不弹出
    def getMin(self) -> int:
        return self.min_stack[-1]


""" (2):使用固定长度的数组实现 """


# 开始我们就以测试的数据量的最大值,来定义这么长的数组
# 没有使用pop,append方法,都是通过索引操作的,这样一定是比上面的要快的
# 提交的时候要注意:把类名改成MinStack
class MinStack2:
    # 这是是左神测试出来的,在力扣上面的测试数据的最大数据量,如果不通过,那么就改大
    k = 8001  # 初始化的队列的最大长度

    # 同时初始化数据栈和最小栈
    def __init__(self):
        self.data = [-1] * self.k  # 初始化一个长度为k的数据栈
        self.min = [-1] * self.k  # 初始化一个长度为k的最小栈
        self.size = 0  # 初始化长度为0,同时size表示栈中已有元素的下一个位置

    # 向栈中加入一个元素value
    def push(self, value):
        self.data[self.size] = value  # 对于数据栈,直接加入到size位置就可以了
        # 对最小栈的压入,需要判断:比较最小栈栈顶和value的关系
        # (1):如果此时最小栈为空;或则是value小于当前最小栈的栈顶元素
        if self.size == 0 or value < self.min[self.size - 1]:
            self.min[self.size] = value  # 那么把value压入到最下栈中
        else:  # (2):最小栈不是空的,且当前栈顶的元素比value还要小(或者相等)
            self.min[self.size] = self.min[self.size - 1]  # 那么把最小栈的栈顶数字再压入到最小栈
        self.size += 1  # 栈的长度+1

    # 弹出栈顶的元素,直接修改size的位置
    def pop(self):
        self.size -= 1  # 直接调整size的位置就可以了

    # 取出栈顶的元素,不弹出
    def top(self):
        return self.data[self.size - 1]  # 返回索引为size-1位置的元素

    # 取出当前栈的最小的元素,不弹出
    def getMin(self):
        return self.min[self.size - 1]  # 直接返回最小栈的栈顶元素
