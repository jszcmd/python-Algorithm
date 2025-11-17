import heapq
from typing import List


# 测试链接:https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/
# 直接把Solution复制到力扣里面,时间复杂度O(N*log N),约300ms左右
# 使用python中heapq中内置的小根堆实现
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        """
        🎯 将数组减半的最少操作次数
        💡 使用最大堆(通过负数模拟)来每次取当前最大值进行减半
        ⏱️ 时间复杂度: O(N log N)
        """
        # 🎯 target_sum --> 要减少的目标（数组总和的一半）
        target_sum: float = sum(nums) / 2

        # 🔄 把nums里面的数都变成负数（用负数模拟最大堆）
        # 💡 因为python内置的堆是小根堆，用负数就可以保证加绝对值之后是大根堆的形式
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)  # ⏱️ O(N) 建堆

        # 📊 cur_sum是已经减少的幅度；ans是操作的次数
        cur_sum: float = 0
        ans = 0

        # 🔄 循环直到减少的幅度达到目标
        while cur_sum < target_sum:
            # 📥 弹出堆顶元素（取负号后就是原数组中的最大值）
            max_num = - heapq.heappop(max_heap)  # ⏱️ O(log N)

            # ➕ 将最大值减半后重新加入堆中
            heapq.heappush(max_heap, - max_num / 2)  # ⏱️ O(log N)

            # 📈 累计减少的幅度
            cur_sum += max_num / 2
            ans += 1

        return ans


# 测试链接:https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/
# 用自己写的大根堆,把类名Solution02改成Solution
# 但是用python内置的优先级队列还要慢
class Solution02:
    def halveArray(self, nums: List[int]) -> int:
        """
        🎯 将数组减半的最少操作次数(手动实现大根堆版本)
        💡 通过位运算避免浮点数精度问题,使用手动实现的大根堆
        ⏱️ 时间复杂度: O(N log N)
        """
        size = len(nums)
        max_heap = [0] * size

        # 🔄 从底到顶建立大根堆,这个过程的时间复杂度O(N)
        for i in range(size - 1, -1, -1):
            # 💡 把数组中的每一个数都*2^20（通过左移20位），避免浮点数精度问题
            max_heap[i] = nums[i] << 20
            self.heapify(max_heap, i, size)  # ⏱️ 向下调整

        # 🎯 target_sum --> 要减少的目标（大数总和的一半）
        target_sum = sum(max_heap) / 2
        ans = 0
        cur_sum = 0

        # 🔄 循环直到减少的幅度达到目标
        while cur_sum < target_sum:
            max_heap[0] /= 2  # ✂️ 堆顶的元素减半
            cur_sum += max_heap[0]  # 📈 增加幅度
            self.heapify(max_heap, 0, size)  # 🔄 向下调整堆 ⏱️ O(log N)
            ans += 1

        return ans

    # 🔧 大根堆调整函数：max_heap[i]位置的元素变小了,需要向下调整维持大根堆特性
    # ⏱️ 时间复杂度: O(log N)
    def heapify(self, max_heap, i, size):
        l = 2 * i + 1  # 👈 左孩子索引

        # 🔄 当有左孩子时继续调整
        while l < size:
            # 🏆 选择左右孩子中较大的那个
            best = l + 1 if l + 1 < size and max_heap[l + 1] > max_heap[l] else l

            # 🔍 比较当前节点和较大的孩子
            best = best if max_heap[best] > max_heap[i] else i

            if best == i: break  # ✅ 当前节点已经比孩子大,无需调整

            # 🔄 交换当前节点和较大的孩子
            max_heap[i], max_heap[best] = max_heap[best], max_heap[i]
            i = best
            l = 2 * i + 1  # 🔄 更新左孩子索引
