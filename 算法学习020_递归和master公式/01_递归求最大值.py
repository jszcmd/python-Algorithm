"""
递归和master公式学习笔记

## 前置知识：无

1. 从思想上理解递归:对于新手来说,递归去画调用图是非常重要的,有利于分析递归
2. 从实际上理解递归:递归不是玄学,底层是利用系统栈来实现的
3. 任何递归函数都一定可以改成非递归,不用系统帮你压栈(系统栈空间),自己压栈呗(内存空间)
4. 递归改成非递归的必要性:
   a. 工程上几乎一定要改,除非确定数据量再大递归也一定不深,归并排序、快速排序、线段树、很多的平衡树等,后面都讲
   b. 算法尝试或者比类中(能通过就不改)
5. master公式
   a. 所有子问题规模相同的递归才能用master公式,\( T(n) = a * T(n/b) + 0(n^c) \)，a、b、c都是常数
   b. 如果log(b,a) < c,复杂度为: 0(n^c)
   c. 如果log(b,a) > c,复杂度为: 0(n^log(b,a))
   d. 如果log(b,a) == c,复杂度为: 0(n^c * logn)
6. 一个补充
    T(n) = 2*T(n/2) + 0(n*logn) ,时间复杂度是0(n * ((logn)的平方)),证明过程比较复杂,记住即可
"""


# Master公式分析本算的时间复杂度
# a = 2, b = 2, c = 0
# log(b,a) = log(2,2) = 1 > c = 0
# 时间复杂度为：O(n^log(2,2)) = O(n)

# 使用分治算法求数组最大值的主函数
def max_value(arr):
    return f(arr, 0, len(arr) - 1)


# 在arr[l,r]上找到最大值
def f(arr: list[int], l: int, r: int) -> int:
    """
    :param arr: 目标数组
    :param l: 索引为l的整数
    :param r: 索引为r的整数
    :return: 返回值的类型为int,l到r范围的最大值
    """
    # 🎯 Base Case: 当范围内只有一个元素时
    if l == r: return arr[l]  # 递归结束条件

    # 🎯 计算中间位置(使用整数除法)
    m = (l + r) // 2

    # 🎯 递归求解左右两半的最大值
    lmax = f(arr, l, m)  # 左半部分最大值
    rmax = f(arr, m + 1, r)  # 右半部分最大值

    # 🎯 合并结果：返回左右两部分的最大值
    return lmax if lmax > rmax else rmax


if __name__ == "__main__":
    arr = [3, 8, 7, 6, 4, 5, 1, 2]
    print("数组最大值:", max_value(arr))
