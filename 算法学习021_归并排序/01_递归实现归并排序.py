""" 填函数练习风格 """
# 测试链接:https://leetcode.cn/problems/sort-an-array/
# 直接把下面的Solution类复制到力扣里面
# 当然用python的运行速度是很慢的,时间约1000ms组左右,打败5%左右的人;
from typing import List


class Solution:
    help = [0] * 50001  # 定义一个辅助数组,长度够用

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, l, r):
        if l == r: return  # base_case:左边和右边相等,退出
        m = (l + r) // 2  # 取l和r的中点,注意l,m,r都是整数,这里要用//取整
        self.mergeSort(nums, l, m)  # 把左边l到m位置变得有序;
        self.mergeSort(nums, m + 1, r)  # 把右边m+1到l位置变得有序;
        self.merge(nums, l, m, r)  # 把nums数组l到r整体变得有序;

    # 把l到r位置整体变得有序;
    def merge(self, nums, l, m, r):
        a = l  # 变量a,记录左边的位置
        i = l  # 变量i,刷到help辅助数组中的位置
        b = m + 1  # 变量b,记录右边的数的位置
        # 左边和右边的谁小拷贝谁,
        while a <= m and b <= r:  # 左边和右边都没有越界
            if nums[a] <= nums[b]:  # 左边<=右边
                self.help[i] = nums[a]  # 把左边的数刷到help数组中
                i += 1  # i++,i位置后移
                a += 1  # a++,a位置也后移
            else:  # 左边大于右边
                self.help[i] = nums[b]  # 把右边的数刷到help数组中;
                i += 1  # i++,i位置后移
                b += 1  # b++,b位置也后移
        # 从上面这个while循环里面出来以后,必有一个索引越界,就把那个不越界的刷到help数组中;
        while a <= m:  # 左边剩下还有数,把左边剩下的数都刷到help数组
            self.help[i] = nums[a]
            i += 1
            a += 1
        while b <= r:  # 右边剩下还有数,把右边剩下的数都刷到help数组
            self.help[i] = nums[b]
            i += 1
            b += 1
        for i in range(l, r + 1):  # 把help数组[l,r]位置的数都刷回到原数组nums中
            nums[i] = self.help[i]


""" acm练习风格:处理输入输出 """
# 测试链接:https://www.luogu.com.cn/problem/P1177
# 直接把下面的一整块都复制到洛谷的里面

import sys
from typing import List  # 需要导入List


class Solution02:
    help = [0] * 100001  # 定义一个辅助数组,长度够用

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums: List[int], l: int, r: int):
        if l == r: return  # base_case:左边和右边相等,退出
        m = (l + r) // 2  # 取l和r的中点,注意l,m,r都是整数,这里要用//取整
        self.mergeSort(nums, l, m)  # 把左边l到m位置变得有序;
        self.mergeSort(nums, m + 1, r)  # 把右边m+1到l位置变得有序;
        self.merge(nums, l, m, r)  # 把nums数组l到r整体变得有序;

    # 把l到r位置整体变得有序;
    def merge(self, nums: List[int], l: int, m: int, r: int):
        a = l  # 变量a,记录左边的位置
        i = l  # 变量i,刷到help辅助数组中的位置
        b = m + 1  # 变量b,记录右边的数的位置
        # 左边和右边的谁小拷贝谁,
        while a <= m and b <= r:  # 左边和右边都没有越界
            if nums[a] <= nums[b]:  # 左边<=右边
                self.help[i] = nums[a]  # 把左边的数刷到help数组中
                i += 1  # i++,i位置后移
                a += 1  # a++,a位置也后移
            else:  # 左边大于右边
                self.help[i] = nums[b]  # 把右边的数刷到help数组中;
                i += 1  # i++,i位置后移
                b += 1  # b++,b位置也后移
        # 从上面这个while循环里面出来以后,必有一个索引越界,就把那个不越界的刷到help数组中;
        while a <= m:  # 左边剩下还有数,把左边剩下的数都刷到help数组
            self.help[i] = nums[a]
            i += 1
            a += 1
        while b <= r:  # 右边剩下还有数,把右边剩下的数都刷到help数组
            self.help[i] = nums[b]
            i += 1
            b += 1
        for i in range(l, r + 1):  # 把help数组[l,r]位置的数都刷回到原数组nums中
            nums[i] = self.help[i]


if __name__ == "__main__":
    # 读取输入
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    # 创建解决方案实例并排序
    solution = Solution02()
    solution.sortArray(arr)  # 原地排序
    # 输出结果
    print(" ".join(map(str, arr)))  # 直接输出已排序的arr
