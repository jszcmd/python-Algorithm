import random
from typing import List


# 经典的随机快速排序
# 直接把这个类复制粘贴到:https://leetcode.cn/problems/sort-an-array/
# 把类名改成Solution,你就会发现过不了,超时
class Solution01:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, arr, l, r):
        # 如果l==r,只有一个数
        # l > r,范围无效
        if l >= r:
            return

        # 从l...r随机选一个位置,x这个值,做划分
        x = arr[random.randint(l, r)]
        mid = self.partiton(arr, l, r, x)
        self.quickSort(arr, l, mid - 1)
        self.quickSort(arr, mid + 1, r)

    def partiton(self, arr, l, r, x):
        a = l
        xi = 0
        # a表示<=x的越界位置,即处理后l到a-1之间的都是<=x的
        for i in range(l, r + 1):
            if arr[i] <= x:
                arr[a], arr[i] = arr[i], arr[a]
                if arr[a] == x:
                    xi = a
                a += 1
        # <=x的区域 l...a-1; >x的区域 a...r
        arr[xi], arr[a - 1] = arr[a - 1], arr[xi]
        return a - 1


# 使用改进版本的随机快速排序:把这个类直接提交
# 类名:Solution,测试链接:https://leetcode.cn/problems/sort-an-array/
class Solution02:
    """"""
    """对外公开的唯一方法用户只能调用这个方法进行排序"""
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) <= 1:
            return nums
        self.__quick_sort(nums, 0, len(nums) - 1)
        return nums

    """私有方法(双下划线)：快速排序实现"""
    def __quick_sort(self, arr: List[int], l: int, r: int) -> None:
        if l >= r:
            return
        # 随机选择枢轴
        x = arr[random.randint(l, r)]
        first, last = self.__partition(arr, l, r, x)
        # 递归排序
        self.__quick_sort(arr, l, first - 1)
        self.__quick_sort(arr, last + 1, r)

    """私有方法(双下划线)：荷兰国旗划分"""
    def __partition(self, arr: List[int], l: int, r: int, x: int) -> tuple[int, int]:
        first = l
        last = r
        i = l
        while i <= last:
            if arr[i] < x:
                arr[first], arr[i] = arr[i], arr[first]
                first += 1
                i += 1
            elif arr[i] == x:
                i += 1
            else:
                arr[last], arr[i] = arr[i], arr[last]
                last -= 1

        return first, last


