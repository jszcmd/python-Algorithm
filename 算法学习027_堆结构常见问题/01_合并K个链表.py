""" 填写函数的风格 """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 牛客测试链接:https://www.nowcoder.com/practice/65cfde9e5b9b4cf2b6bafa5f3ef33fa6
# 注意牛客提交的也要把下面的导包也提交进去;函数名mergeKLists和类名Solution不能改
# 力扣测试链接:https://leetcode.cn/problems/merge-k-sorted-lists/
# 力扣测试提交的时候,导包可要可不要; 注意: 函数名mergeKLists和类名Solution不能改

from heapq import heappush, heappop
from typing import List, Optional


# 使用heapq模块中的小根堆实现的
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        🎯 合并K个有序链表的主函数
        📝 使用最小堆来高效合并多个有序链表
        💡 时间复杂度: O(N log K), 其中N是总节点数, K是链表个数
        🚀 空间复杂度: O(K), 堆的大小最多为链表个数
        """
        # 🎯 创建最小堆,存储三元组：(节点值, 链表索引, 节点)
        heap = []

        # 🔄 初始化堆：将每个链表的头节点加入堆中
        for i, head in enumerate(lists):
            if head:
                # ➕ 将(节点值, 链表索引, 节点)推入堆中
                # 💡 链表索引用于处理节点值相同的情况,避免比较ListNode对象
                heappush(heap, (head.val, i, head))

        # ⚠️ 边界情况: 如果堆为空, 说明所有链表都是空的
        if not heap: return None

        # 🎯 创建虚拟头节点, 简化链表操作
        dummy = cur = ListNode(0)

        # 🔄 循环直到堆为空(所有链表都处理完毕)
        while heap:
            val, i, node = heappop(heap)  # 📥 弹出当前最小的节点
            cur.next = node  # 🔗 将当前节点连接到结果链表
            cur = cur.next  # 更新cur节点
            # ➕ 如果当前节点还有下一个节点, 将其加入堆中继续比较
            if node.next: heappush(heap, (node.next.val, i, node.next))

        return dummy.next  # 🎯 返回合并后的链表头节点


# 力扣测试链接:https://leetcode.cn/problems/merge-k-sorted-lists/
# 注意: 提交的时候把类名改成类Solution
# python用手动实现的效果没有用系统中的heapq实现的好
# 注意:下面的这段代码在牛客中提交是过不了的,牛客的在线IDE认为这个写法有问题

# 自己手写的小根堆实现
class Solution02:
    def __init__(self):
        # 🗂️ 初始化最小堆数组,存储链表节点指针,python底层对ListNode的处理就是处理指针
        self.min_heap: List[Optional[ListNode]] = [None] * 10001
        self.size_heap = 0  # 📊 堆的当前大小

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        🎯 合并K个有序链表的主函数
        📝 使用手动实现的最小堆来合并多个有序链表
        💡 时间复杂度: O(N log K), 其中N是总节点数, K是链表个数
        🚀 空间复杂度: O(K), 堆的大小最多为链表个数
        """
        # ⚠️ 处理空输入
        if not lists: return None

        self.size_heap = 0  # 🔄 重置堆大小

        # 🔄 将所有非空链表的头节点加入最小堆
        for lst in lists:
            if lst:
                self.add_node(lst)

        # ⚠️ 如果堆为空(所有链表都为空)
        if self.size_heap == 0: return None  # 都是空节点的情况

        # 🎯 创建哑节点作为结果链表的起点
        dummy = ListNode(-1)
        cur = dummy

        # 🔁 循环直到堆为空(所有节点都处理完毕)
        while self.size_heap > 0:
            min_node = self.pop_min()  # 📤 弹出当前最小节点
            cur.next = min_node  # 🔗 连接到结果链表
            cur = cur.next  # ➡️ 移动当前指针

            # 🔄 如果该节点还有后续节点,加入堆中继续比较
            if min_node.next: self.add_node(min_node.next)

        return dummy.next

    def add_node(self, x: ListNode):
        """
        📥 向最小堆添加节点
        ⏱️ 时间复杂度: O(logK), 其中K是堆的大小
        """
        self.min_heap[self.size_heap] = x  # ➕ 添加到堆末尾
        i = self.size_heap
        self.size_heap += 1

        # 🔼 向上调整堆
        while i > 0 and self.min_heap[i].val < self.min_heap[(i - 1) // 2].val:
            # 🔄 交换当前节点与父节点
            self.min_heap[(i - 1) // 2], self.min_heap[i] = self.min_heap[i], self.min_heap[(i - 1) // 2]
            i = (i - 1) // 2

    def pop_min(self) -> ListNode:
        """
        📤 弹出堆顶最小节点
        ⏱️ 时间复杂度: O(logK), 其中K是堆的大小
        """
        min_node = self.min_heap[0]  # 🎯 保存堆顶最小节点
        self.size_heap -= 1

        # 🔄 将堆顶与最后一个元素交换
        self.min_heap[0], self.min_heap[self.size_heap] = self.min_heap[self.size_heap], self.min_heap[0]

        i = 0
        l = 2 * i + 1  # 👈 左子节点索引

        # 🔽 向下调整堆
        while l < self.size_heap:
            # 🎯 找出左右子节点中值较小的
            best = l + 1 if (l + 1 < self.size_heap and self.min_heap[l + 1].val < self.min_heap[l].val) else l
            # ⚖️ 比较当前节点与较小子节点
            best = best if self.min_heap[best].val < self.min_heap[i].val else i
            # ✅ 如果堆性质已满足，退出循环
            if best == i: break
            # 🔄 交换当前节点与较小子节点
            self.min_heap[best], self.min_heap[i] = self.min_heap[i], self.min_heap[best]
            i = best
            l = 2 * i + 1

        return min_node
