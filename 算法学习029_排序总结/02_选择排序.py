## 选择排序

def select_sort(arr: list[int]) -> list[int]:
    """
    🎯 选择排序算法
    📌 每轮选择最小的元素放到已排序序列的末尾
    ⏱️ 时间复杂度: O(n²)
    💾 空间复杂度: O(1)
    📊 稳定性: 不稳定

    Args: arr:待排序的整数列表

    Returns:排序后的整数列表 (原地修改)
    """
    n = len(arr)
    if n < 1: return arr
    # 🔁 外层循环:遍历每个位置
    # 🎯 为每个位置选择合适的最小元素
    for i in range(n):
        min_index = i  # 🎯 假设当前位置是最小值

        # 🔍 内层循环:在未排序部分中寻找真正的最小值
        # 📈 从 i+1 开始到数组末尾
        for j in range(i + 1, n):
            # 🎯 如果找到更小的元素,更新最小值索引
            if arr[j] < arr[min_index]:
                min_index = j

        # 🔄 将找到的最小元素与当前位置交换
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 🧪 测试示例
if __name__ == "__main__":
    test_arr = [64, 25, 12, 22, 11]
    print("🧪 原始数组:", test_arr)

    sorted_arr = select_sort(test_arr)
    print("✅ 排序结果:", sorted_arr)

    # 🎯 执行过程示例:
    # 第1轮: [11, 25, 12, 22, 64]  ← 找到最小值11与64交换
    # 第2轮: [11, 12, 25, 22, 64]  ← 找到最小值12与25交换  
    # 第3轮: [11, 12, 22, 25, 64]  ← 找到最小值22与25交换
    # 第4轮: [11, 12, 22, 25, 64]  ← 25已在正确位置
    # 第5轮: [11, 12, 22, 25, 64]  ← 排序完成