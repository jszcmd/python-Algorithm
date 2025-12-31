"""
======================================================================================
题目: 2127. 参加会议的最多员工数 (Maximum Employees to Be Invited to a Meeting)
测试链接: https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/description/
难度: 困难 (Hard)
来源: LeetCode

描述:
一个公司准备组织一场会议, 邀请名单上有 n 位员工。
公司准备了一张 圆形 的桌子, 可以坐下 任意数目 的员工。

员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工, 每位员工 当且仅当 他被安排在喜欢员工的旁边,
他才会参加会议。每位员工喜欢的员工 不会 是他自己。

给你一个下标从 0 开始的整数数组 favorite , 其中 favorite[i] 表示第 i 位员工喜欢的员工。
请你返回参加会议的 最多员工数目。
======================================================================================
"""

from typing import List
from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # favorite数组本身就可以表示图: favorite[a]=b : a --> b
        n = len(favorite)  # 人数
        # 入度表
        indegree = [0] * n  # 入度表,0位置也使用
        # 拓扑排序需要的队列
        queue = deque()  # 使用collections库中的队列
        # 深度链数组
        deep = [0] * n  # deep[i]不包括i在内,i之前的最长链的长度

        # 先统计入度表
        for i in range(n):
            indegree[favorite[i]] += 1
        # 先把入度为0的点加入到队列里面
        for i in range(n):
            if indegree[i] == 0: queue.append(i)  # 把入度为0的点加入到队列里面

        # 拓扑排序的主要逻辑
        while queue:
            cur = queue.popleft()  # 弹出入度为0的节点
            next = favorite[cur]  # cur喜欢的人(cur的邻居)
            indegree[next] -= 1  # next节点的入度-1
            deep[next] = max(deep[next], deep[cur] + 1)  # 维持最长链的长度
            if indegree[next] == 0: queue.append(next)  # 把入度为0的邻居加入到队列里面
        """ 拓扑排序结束以后,目前,不在环上的点,都删除了!!! 不在环上面的节点i : indegree[i] = 0. """

        # 可能性1: 所有小环(中心个数 == 2), 算上中心点 + 延伸点 总个数
        sumOfSmallRings = 0
        # // 可能性2: 所有大环(中心个数 > 2), 只算中心点, 最大环中心点个数
        bigRings = 0
        # 再遍历一遍所有节点,只关心环
        for i in range(n):
            if indegree[i] > 0:
                ringSize = 1
                indegree[i] = 0
                j = favorite[i]
                while j != i:  # 只要是j不等于i,就一直绕圈
                    ringSize += 1
                    indegree[j] = 0  # 沿途把入度改成0,一个环只绕一次
                    j = favorite[j]  # 一直绕圈
                if ringSize == 2:  # 遇到小环
                    sumOfSmallRings += 2 + deep[i] + deep[favorite[i]]  # 小环累加
                else:  # 遇到大环
                    bigRings = max(bigRings, ringSize)  # 大环取最大值

        return max(sumOfSmallRings, bigRings)
