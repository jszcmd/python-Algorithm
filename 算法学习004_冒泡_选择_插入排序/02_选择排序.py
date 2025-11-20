"""选择排序"""

"""
选择排序思想:(升序5个元素)
第一轮:对全部元素,在未排列的序列中选中最小的元素,存放在序列的起始位置
第二轮:对剩余元素,在未排列的序列中选中最小的元素,存放在已排序的序列的末尾
第三轮:对剩余元素,在未排列的序列中选中最小的元素,存放在已排序的序列的末尾
...

时间复杂度:O(n²)
空间复杂度:O(1)
稳定性:不稳定
"""


def select_sort(arr: list[int]) -> list[int]:
    """
    选择排序算法实现
    Args: arr: 待排序的整数列表
    Returns: 排序后的整数列表
    """
    n = len(arr)  # 获取数组长度

    # 遍历所有数组元素，最后一个元素会自动就位,所以只需要n-1次
    for i in range(0, n - 1):
        min_index = i  # 假设当前索引i处的元素是最小值

        # 在剩余未排序部分中寻找真正的最小值
        for j in range(i + 1, n):
            # 如果找到更小的元素,更新最小值的索引
            if arr[j] < arr[min_index]:
                min_index = j

        # 将找到的最小元素与当前位置i的元素交换
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # 打印每一轮排序后的结果，便于观察排序过程
        print(f"第{i + 1}轮后的结果:", arr)

    return arr


# 测试数据
arr = [64, 25, 12, 22, 11]

# 调用选择排序函数
print("原始数组:", arr)
select_sort(arr)
print("最终排序结果:", arr)
