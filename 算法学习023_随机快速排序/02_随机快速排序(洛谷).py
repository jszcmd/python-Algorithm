import random
from typing import List


# 测试链接:https://www.luogu.com.cn/problem/P1177
# 可以把下面的8-66行直接复制到洛谷里面运行

class Solution:
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


def main():
    # 读取输入
    n = int(input().strip())  # 第一行：数组长度
    arr = list(map(int, input().split()))  # 第二行：数组元素，用空格分隔
    # map(int,...)将字符串列表中的每一个元素转成整型,

    # 创建解决方案对象并排序
    solution = Solution()
    sorted_arr = solution.sortArray(arr)

    # 输出排序结果
    print(' '.join(map(str, sorted_arr)))
    # 将整型数组转成字符串数组,然后拼接打印


if __name__ == "__main__":
    main()
