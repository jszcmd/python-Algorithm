import random
from typing import List


# 注意:这个经典的随机快速排序在力扣/洛谷中测试过不了
# 超时!!!!
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        🚀 数组排序主入口:采用随机化快速排序算法,高效解决排序问题
        💫 参数: nums: 待排序的整数数组
        🌟 返回: 原地排序后的数组
        """
        # 🎯 基础情况处理：空数组或单元素数组已有序
        if len(nums) <= 1: return nums

        # 🔥 启动快速排序引擎
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, arr: list[int], l: int, r: int) -> None:
        """
        ⚡ 快速排序核心递归函数
        采用分治策略，将大问题分解为小问题解决
        🎪 参数:
            arr: 待排序数组
            l:   当前处理区间的左边界
            r:   当前处理区间的右边界
        """
        # 🛑 递归终止条件：区间无效或只剩单个元素
        if l >= r: return

        # 🎲 魔法所在:随机选择基准值,避免最坏情况
        #    让排序过程充满惊喜
        x: int = arr[random.randint(l, r)]

        # 🎯 执行分区操作,找到基准值的正确位置
        mid: int = self.partition(arr, l, r, x)

        # 🌈 递归征服左右两个子区间
        self.quickSort(arr, l, mid - 1)  # ← 左半场精彩继续
        self.quickSort(arr, mid + 1, r)  # → 右半场同样出色

    def partition(self, arr: list[int], l: int, r: int, x: int) -> int:
        """
        🎪 分区表演秀：将数组重新排列为三部分
        [小于等于x的元素] + [x] + [大于x的元素]
        🎯 参数:
            arr: 待分区数组
            l:   分区左边界
            r:   分区右边界
            x:   基准值明星
        🌟 返回: 基准值在排序后的最终王座位置
        """
        # 🎪 初始化分区状态
        a: int = l  # 🎯 <=x 区域的边界守卫
        xi: int = 0  # 📍 记录任意一个x的位置宝藏

        # 🎡 开始精彩的分区巡游
        for i in range(l, r + 1):
            if arr[i] <= x:
                # 🎭 元素交换魔术：将<=x的元素移到左侧区域
                arr[a], arr[i] = arr[i], arr[a]

                # 📍 如果发现x的踪迹,立即标记位置
                if arr[a] == x: xi = a  # 记录一个x

                a += 1  # 🚀 扩展<=x王国的疆域
            # 💫 大于x的元素暂时保持原位,稍后处理

        # 🎊 分区完成!现在进行最后的王座交接仪式
        #    将基准值x请到它应有的王座位置
        arr[a - 1], arr[xi] = arr[xi], arr[a - 1]

        return a - 1  # 🏆 返回基准值的荣耀王座
