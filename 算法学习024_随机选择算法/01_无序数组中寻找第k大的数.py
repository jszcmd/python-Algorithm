import random
from typing import List

""" 力扣测试(填函数风格) """


# 测试链接:https://leetcode.cn/problems/kth-largest-element-in-an-array/
# 直接把下面的Solution类复制到力扣里面就可以了

class Solution:
    first: int = 0  # 🎯 分区左边界:记录等于基准值的起始位置
    last: int = 0  # 🎯 分区右边界:记录等于基准值的结束位置

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        🔍 寻找数组中第K大的元素

        💡 核心思路：
            - 第1大 = 最大的数 = 排序后最后一个位置的数
            - 第k大 = 排序后第(len(nums)-k)位置的数

        📌 参数:
            nums: 整数数组
            k: 要查找的第k大元素的排名

        📊 返回:第k大的元素值
        """
        # 第k大元素在排序后的位置索引 = 数组长度 - k
        target_index = len(nums) - k
        return self.randomizedSelect(nums, target_index)

    def randomizedSelect(self, arr: list[int], target_index: int) -> int:
        """
        🎯 随机选择算法：找到排序后会在target_index位置的元素

        💡 算法思想：
            - 使用快速选择算法,类似快速排序但只处理包含目标的那一半
            - 平均时间复杂度：O(n),最坏情况:O(n²)

        📌 参数:
            arr: 输入数组
            target_index: 目标位置索引

        📊 返回:
            排序后会在target_index位置的元素值
        """
        ans: int = 0  # 🎯 存储最终结果
        l: int = 0  # 🔰 当前搜索区间的左边界
        r: int = len(arr) - 1  # 🔰 当前搜索区间的右边界

        # 🔄 在区间[l, r]中寻找目标元素
        while l <= r:
            # 🎲 随机选择基准值并进行三路分区
            pivot = arr[random.randint(l, r)]
            self.partition(arr, l, r, pivot)

            # 📍 根据目标位置与分区边界的关系调整搜索区间
            if target_index < self.first:
                # 🎯 目标在左分区(小于基准值的区域)
                r = self.first - 1
            elif target_index > self.last:
                # 🎯 目标在右分区(大于基准值的区域)
                l = self.last + 1
            else:
                # 🎉 找到目标！目标在等于基准值的区域内
                ans = arr[target_index]
                break

        return ans

    def partition(self, arr: list[int], l: int, r: int, pivot: int) -> None:
        """
        🏴‍☠️ 荷兰国旗三路分区算法

        💡 将数组arr[l..r]划分为三个区域：
            - [l, first-1] : 小于pivot的元素
            - [first, last] : 等于pivot的元素
            - [last+1, r]   : 大于pivot的元素

        🎯 算法过程：使用三个指针：first、last、i 来维护三个区域的边界

        📌 参数:
            arr: 待分区数组
            l: 分区左边界
            r: 分区右边界
            pivot: 基准值
        """
        self.first = l  # 🎯 初始化:小于区域的右边界
        self.last = r  # 🎯 初始化:大于区域的左边界
        i: int = l  # 🔍 遍历指针

        # 🔄 遍历当前分区区间
        while i <= self.last:
            if arr[i] == pivot:
                # ✅ 当前元素等于基准值,留在中间区域,继续向后扫描
                i += 1
            elif arr[i] < pivot:
                # 🔄 当前元素小于基准值,交换到左区域
                arr[i], arr[self.first] = arr[self.first], arr[i]
                self.first += 1  # 🎯 扩大小于区域
                i += 1  # 🔍 继续扫描下一个元素
            else:
                # 🔄 当前元素大于基准值,交换到右区域
                arr[i], arr[self.last] = arr[self.last], arr[i]
                self.last -= 1  # 🎯 扩大大于区域
                # ⚠️ 注意：这里不增加i,因为需要检查从右边交换过来的新元素
