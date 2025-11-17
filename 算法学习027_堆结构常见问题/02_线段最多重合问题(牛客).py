# 测试链接:https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37
# 牛客的测试链接需要自己处理输入与输出,把下面的所有的代码都复制到牛客,我们用的是自己写的小根堆

import sys


class Solution:
    def max_overlap(self, arr_line: list[list[int]]) -> int:
        """
        🎯 计算线段的最大重叠数量
        ⏱️ 时间复杂度: O(n log n)
        💾 空间复杂度: O(n)
        """
        ans: int = 0  # 🏆 最终要返回的结果 - 最大重叠线段数量
        min_heap = []  # 🎯 小根堆用于存储线段的结束位置（堆顶是最早结束的时间）
        # 🔄 所有线段根据开始位置排序
        arr_line.sort(key=lambda x: x[0])

        for start, end in arr_line:
            # 🗑️ 移除所有已结束的线段
            while min_heap and min_heap[0] <= start:
                self.pop_min(min_heap)

            # ➕ 将当前线段的结束位置加入堆
            self.add(min_heap, end)
            # 📈 更新最大重合数量
            ans = max(ans, len(min_heap))
        return ans

    """
    🗑️ 弹出小根堆的第一个堆顶元素  ⏱️ 时间复杂度: O(log n)
    """

    def pop_min(self, min_heap):
        if not min_heap: return

        # 🔄 把堆顶元素和最后一个元素交换
        min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
        # 🗑️ 移除最后一个元素(原堆顶)
        min_heap.pop()

        size = len(min_heap)
        i = 0  # 📍 从堆顶开始调整
        l = 2 * i + 1  # 👈 左子节点索引

        while l < size:
            # 🏆 找到左右子节点中较小的那个
            best = l + 1 if (l + 1 < size and min_heap[l + 1] < min_heap[l]) else l
            # 🔍 比较当前节点和较小子节点
            best = best if min_heap[best] < min_heap[i] else i
            if best == i: break  # ✅ 无需调整，退出循环
            # 🔄 交换位置
            min_heap[i], min_heap[best] = min_heap[best], min_heap[i]
            i = best
            l = 2 * i + 1  # 🔄 更新左子节点索引

    """
    ➕ 向小根堆加入一个元素x  ⏱️ 时间复杂度: O(log n)
    """

    def add(self, min_heap, x):
        # ➕ 将新元素添加到堆的末尾
        min_heap.append(x)
        i = len(min_heap) - 1  # 📍 新元素的索引

        # 🔼 向上调整,维持小根堆性质
        while i > 0 and min_heap[i] < min_heap[(i - 1) // 2]:
            min_heap[i], min_heap[(i - 1) // 2] = min_heap[(i - 1) // 2], min_heap[i]
            i = (i - 1) // 2  # 🔼 移动到父节点


if __name__ == '__main__':
    # 📥 读取线段数量
    n = int(sys.stdin.readline().strip())

    # 📝 初始化空列表
    arr_line = []

    # 🔄 循环读取每条线段的坐标并添加到列表
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().strip().split())
        arr_line.append([start, end])

    solution = Solution()
    print(solution.max_overlap(arr_line))
