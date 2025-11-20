"""冒泡排序"""


# 方式一:正向遍历
def bubble_sort1(arr):
    """
    外层循环控制轮数，从0到n-2
    """
    n = len(arr)
    for i in range(n - 1):  # 需要n-1轮
        for j in range(0, n - 1 - i):  # 每轮比较范围递减
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 方式二:反向遍历
def bubble_sort2(arr):
    """
    外层循环控制边界,从n-1递减到1
    """
    n = len(arr)
    for i in range(n - 1, 0, -1):  # 边界从n-1递减到1
        for j in range(0, i):  # 比较0到i-1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 测试
arr1 = [3, 1, 5, 8, 2]
arr2 = [3, 1, 5, 8, 2]

bubble_sort1(arr1)
bubble_sort2(arr2)

print("方式一结果:", arr1)  # [1, 2, 3, 5, 8]
print("方式二结果:", arr2)  # [1, 2, 3, 5, 8]
