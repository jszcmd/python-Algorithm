""" 填函数练习风格 """
# 测试链接:https://leetcode.cn/problems/sort-an-array/
# 直接把下面的Solution类复制到力扣里面
# 当然用python的运行速度是很慢的,时间约1000ms组左右,打败5%左右的人;
from typing import List


class Solution:
    help = [0] * 50001  # 定义一个辅助数组,长度够用

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums

    # 时间复杂度: O(n * log n);这样就不需要其他太多的参数了;
    def mergeSort(self, nums):
        step = 1  # 步长初始化为1
        n = len(nums)  # 计算数组的长度
        # 外层while循环执行log n次,
        while step < n:
            l = 0
            # 内层while循环对n个数进行操作,O(n);
            while l < n:
                # l是左部分的开头位置的索引值,m是左部分的结束位置索引值
                m = l + step - 1  # m = min(l+step - 1, n - 1)
                # 既然下面都比较的右侧部分的结束位置,那么为什么不比较左侧部分的结束位置?
                # 因为没有必要,如果左侧的结束位置越界(右侧一定越界,一定没有右侧),那么直接把左侧仅有的留在原地,
                # m+1就是右部分的开头位置;
                if m + 1 >= n: break  # m+1>n-1(数组最大索引),超过了,没有右侧部分(那么这一轮的左右不比较,还是把左侧部分留在原地)
                # 正常情况下,m+1+step-1也就是l+2*step-1是右部分的的结束位置,但是可能越界了,超过n-1(最大的索引位置)
                r = min(l + (step * 2) - 1, n - 1)  # 比较l+(step*2) - 1和n-1哪一个更小,哪一个就是右侧部分的结束位置
                self.merge(nums, l, m, r)  # 把数组l到r位置变得有序
                l = r + 1  # 更新l,为下一趟的左右部分比较做准备;
            step <<= 1
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
        self.mergeSort(nums)
        return nums

    # 时间复杂度: O(n * log n);这样就不需要其他太多的参数了;
    def mergeSort(self, nums):
        step = 1  # 步长初始化为1
        n = len(nums)  # 计算数组的长度
        # 外层while循环执行log n次,
        while step < n:
            l = 0
            # 内层while循环对n个数进行操作,O(n);
            while l < n:
                # l是左部分的开头位置的索引值,m是左部分的结束位置索引值
                m = l + step - 1  # m = min(l+step - 1, n - 1)
                # 既然下面都比较的右侧部分的结束位置,那么为什么不比较左侧部分的结束位置?
                # 因为没有必要,如果左侧的结束位置越界(右侧一定越界,一定没有右侧),那么直接把左侧仅有的留在原地,
                # m+1就是右部分的开头位置;
                if m + 1 >= n: break  # m+1>n-1(数组最大索引),超过了,没有右侧部分(那么这一轮的左右不比较,还是把左侧部分留在原地)
                # 正常情况下,m+1+step-1也就是l+2*step-1是右部分的的结束位置,但是可能越界了,超过n-1(最大的索引位置)
                r = min(l + (step * 2) - 1, n - 1)  # 比较l+(step*2) - 1和n-1哪一个更小,哪一个就是右侧部分的结束位置
                self.merge(nums, l, m, r)  # 把数组l到r位置变得有序
                l = r + 1  # 更新l,为下一趟的左右部分比较做准备;
            step <<= 1
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


if __name__ == "__main__":
    # 读取输入
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    # 创建解决方案实例并排序
    solution = Solution02()
    solution.sortArray(arr)  # 原地排序
    # 输出结果
    print(" ".join(map(str, arr)))  # 直接输出已排序的arr
