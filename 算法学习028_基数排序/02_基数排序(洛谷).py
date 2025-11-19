""" ACM风格测试 """
# 测试链接:https://www.luogu.com.cn/problem/P1177
# 直接把这个文件复制到洛谷里面就可以了
# 在洛谷中要处理处理所有数字相同的情况的情况!!!

from typing import List
import sys


class Solution:
    def __init__(self):
        # 🔢 定义基数排序的基数(BASE进制)
        self.BASE: int = 1000
        # 🗂️ 辅助数组,用于临时存储排序结果,大小为50001
        self.help: List[int] = [0] * 100001
        # 📊 计数器数组,用于统计每个数字的出现次数
        self.cnts: List[int] = [0] * self.BASE

    def sortArray(self, nums: List[int]) -> List[int]:
        # ⚡ 边界情况处理:如果数组长度小于等于1,直接返回
        if len(nums) <= 1: return nums

        # 🔍 找到数组中的最小值,用于处理负数
        min_num = min(nums)
        # 🔄 将所有数转换为非负数(减去最小值)
        nums = [x - min_num for x in nums]
        # 📈 找到转换后的最大值,用于确定需要排序的位数
        max_num = max(nums)

        # 🎯 调用基数排序对非负数数组进行排序
        bits_count = self.bits(max_num)
        if bits_count == 0:  # 💡 修复:处理所有数字相同的情况
            bits_count = 1
        self.radixSort(nums, len(nums), bits_count)

        # ↩️ 恢复原始数值(加回之前减去的min_num)
        nums = [x + min_num for x in nums]
        return nums

    def bits(self, number: int) -> int:
        """🧮 计算数字在BASE进制下的位数"""
        ans: int = 0
        while number > 0:
            ans += 1  # 位数加1
            number //= self.BASE  # 除以基数,去掉最低位
        return ans

    def radixSort(self, arr: List[int], n: int, bits: int) -> None:
        """🚀 基数排序的核心实现"""
        offset: int = 1  # 用于提取不同位数的偏移量

        # 🔄 从最低位到最高位依次进行排序
        while bits > 0:
            # 🧹 每轮开始前清空计数器数组
            for i in range(self.BASE):  # 💡 修复：使用循环清空而不是重新创建
                self.cnts[i] = 0

            # 1️⃣ 第一步:数字的词频统计
            # 📈 统计当前位上每个数字(0-9)的出现次数
            for i in range(n):
                # 🔍 提取当前位的数字并增加对应计数
                self.cnts[(arr[i] // offset) % self.BASE] += 1

            # 2️⃣ 第二步:处理成前缀次数累加的形式
            # 📊 此时cnts[i]表示小于等于i的数字有多少个
            for i in range(1, self.BASE):
                self.cnts[i] = self.cnts[i - 1] + self.cnts[i]

            # 3️⃣ 第三步:开始分区,从右往左遍历(保证排序的稳定性)
            # 🎯 根据计数器的位置信息,将元素放入辅助数组的正确位置
            for i in range(n - 1, -1, -1):
                # 🔢 提取当前位的数字
                digit = (arr[i] // offset) % self.BASE
                # 💡 关键步骤:先减1再使用位置,确保每个元素放入唯一位置
                self.cnts[digit] -= 1
                # 📥 将元素放入辅助数组的对应位置
                self.help[self.cnts[digit]] = arr[i]

            # 4️⃣ 第四步:将排序结果从辅助数组复制回原数组
            for i in range(n):
                arr[i] = self.help[i]

            # ⏫ 移动到下一位
            offset *= self.BASE
            # ⏬ 减少剩余位数计数
            bits -= 1


if __name__ == "__main__":
    # 读取输入
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    # 创建解决方案实例并排序
    solution = Solution()
    sorted_arr = solution.sortArray(arr)  # 💡 修复：使用返回值而不是原地修改
    # 输出结果
    print(" ".join(map(str, sorted_arr)))  # 直接输出已排序的arr
