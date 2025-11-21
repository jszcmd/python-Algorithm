""" 递归实现的归并排序 """


# 时间复杂度:O(n * log(n))
# 空间复杂度:O(n)
# 有稳定性

class MergeSort:
    """ 🔄 归并排序类 - 在初始化时对传入数组进行原地排序"""

    def __init__(self, arr: list[int]) -> None:
        """
        🎯 作用: 初始化并立即对数组进行排序
        📥 参数: arr - 待排序的整数数组(会被原地修改)
        📤 返回值: 无
        """
        self.arr = arr
        self.help = [-1] * len(arr)  # 🛠️ 辅助数组,用于归并操作
        if len(arr) <= 1: return  # ⚡ 边界情况处理
        self.mergeSort(arr, 0, len(arr) - 1)  # 🚀 启动归并排序

    def mergeSort(self, arr: list[int], l: int, r: int) -> None:
        """
        🔄 作用: 递归实现归并排序
        📥 参数: arr - 待排序数组, l - 左边界, r - 右边界
        📤 返回值: 无
        """
        if l >= r: return  # ⚡ 递归终止条件
        m: int = (l + r) // 2  # 📍 计算中间位置
        self.mergeSort(arr, l, m)  # 🔁 递归排序左半部分
        self.mergeSort(arr, m + 1, r)  # 🔁 递归排序右半部分
        self.merge(arr, l, m, r)  # 🔗 合并两个有序子数组

    def merge(self, arr: list[int], l: int, m: int, r: int) -> None:
        """
        🔗 作用: 合并两个有序子数组
        📥 参数: arr - 待合并数组, l - 左边界, m - 中间位置, r - 右边界
        📤 返回值: 无
        """
        a: int = l  # 🎯 左子数组指针
        b: int = m + 1  # 🎯 右子数组指针
        i: int = l  # 🎯 辅助数组指针

        # 🔄 比较并合并两个子数组
        while a <= m and b <= r:
            if arr[a] <= arr[b]:
                self.help[i] = arr[a]  # 📥 选择左子数组元素
                a += 1
                i += 1
            else:
                self.help[i] = arr[b]  # 📥 选择右子数组元素
                b += 1
                i += 1

        # 📦 处理左子数组剩余元素
        while a <= m:
            self.help[i] = arr[a]
            a += 1
            i += 1

        # 📦 处理右子数组剩余元素
        while b <= r:
            self.help[i] = arr[b]
            b += 1
            i += 1

        # 📤 将合并结果复制回原数组
        for i in range(l, r + 1):
            arr[i] = self.help[i]


def merge_sort(arr: list[int]) -> list[int]:
    """
    🚀 作用: 对数组进行归并排序（原地修改）
    📥 参数: arr - 待排序的整数数组
    📤 返回值: 无
    """
    MergeSort(arr)  # 🎯 创建匿名对象,自动完成排序和销毁
    return arr
