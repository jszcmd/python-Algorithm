import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 测试链接:https://leetcode.cn/problems/merge-k-sorted-lists/
# 直接把这个类复制到力扣就可以通过了,不是很快10ms左右
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        🎯 合并K个有序链表的主函数
        📝 使用最小堆来高效合并多个有序链表
        💡 时间复杂度: O(N log K)，其中N是总节点数，K是链表个数
        """
        return self._merge(lists)

    # 🔒 定义成一个私有函数,告诉其他人不要直接调用我这个函数
    def _merge(self, lists):
        """
        🛠️ 实际执行合并操作的私有方法
        📚 使用最小堆来维护当前所有链表的最小值
        """
        # 🎯 创建最小堆，存储三元组：(节点值, 链表索引, 节点)
        heap: list[tuple[int, int, ListNode]] = []

        # 🔄 初始化堆：将每个链表的头节点加入堆中
        for i, head in enumerate(lists):
            if head:
                # ➕ 将(节点值, 链表索引, 节点)推入堆中
                # 💡 链表索引用于处理节点值相同的情况,避免比较ListNode对象
                heapq.heappush(heap, (head.val, i, head))

        # ⚠️ 边界情况:如果堆为空,说明所有链表都是空的
        if not heap: return None

        # 🎯 创建虚拟头节点,简化链表操作
        dummy = current = ListNode(0)  # 🏷️ 多1个节点作为起始点

        # 🔄 循环直到堆为空(所有链表都处理完毕)
        while heap:
            # 📥 弹出当前最小的节点
            val, i, node = heapq.heappop(heap)

            # 🔗 将当前节点连接到结果链表
            current.next = node  # ✅ 统一操作
            current = node  # 📍 移动当前指针

            # ➕ 如果当前节点还有下一个节点,将其加入堆中
            if node.next: heapq.heappush(heap, (node.next.val, i, node.next))

        # 🎯 返回合并后的链表头节点(跳过dummy节点)
        return dummy.next
