"""
======================================================================================
题目: 2050. 并行课程 III (Parallel Courses III)
难度: 困难 (Hard)
来源: LeetCode
#### 测试链接: https://leetcode.cn/problems/parallel-courses-iii/

描述:
给你一个整数 n , 表示有 n 节课, 课程编号从 1 到 n .
同时给你一个二维整数数组 relations , 其中 relations[j] = [prevCourse_j, nextCourse_j] ,
表示课程 prevCourse_j 必须在课程 nextCourse_j 之前 完成(先修课的关系).
同时给你一个下标从 0 开始的整数数组 time , 其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数.

请你根据以下规则算出完成所有课程所需要的 最少 月份数:
1. 如果一门课的所有先修课都已经完成, 你可以在 任意 时间开始这门课程.
2. 你可以 同时 上 任意门课程 .

请你返回完成所有课程所需要的 最少 月份数.

注意: 测试数据保证一定可以完成所有课程(也就是先修课的关系构成一个有向无环图).
======================================================================================
"""

from typing import List


class Solution:
    MAX = 50001  # 最大的节点数,同时也是最大的边的数量
    # 链式前向星建图所需要的变量
    head: list[int] = [0] * MAX
    next: list[int] = [0] * MAX
    to: list[int] = [0] * MAX
    cnt: int = 0

    # 拓扑排序需要的队列
    queue: list[int] = [0] * MAX
    l: int = 0  # 队列头部的指针
    r: int = 0  # 队列尾部的指针

    # 入度表 下标 1-n
    indegree: list[int] = [0] * MAX  # 0位置弃而不用

    # 花费表 cost[i]: 表示完成课程i,以及其前面的课程所需要的时间
    cost: list[int] = [0] * MAX

    # 初始化函数
    def build(self) -> None:
        self.l = self.r = 0  # 初始化队列
        self.cnt = 1  # 边的编号从1开始,这样0就可以表示"没有边"
        self.head = [0] * self.MAX  # 初始化头指针数组
        self.indegree = [0] * self.MAX  # 清空入度表
        self.cost = [0] * self.MAX  # 清空花费表

    # 建图,添加边的函数
    def addChainEdge(self, u: int, v: int) -> None:
        self.next[self.cnt] = self.head[u]  # 新边的next指向旧的头部head[u]
        self.to[self.cnt] = v  # 第cnt条边的终点是v
        self.head[u] = self.cnt  # 更新节点u的新边,为:第cnt条边
        self.cnt += 1  # cnt++,为下一条边做准备

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # n:节点的个数  节点的关系[1,2,3,...,n]节点是从1开始的, 一共有 1,2,...,n这么多个节点
        # 时间time:  0下标: time[0] 代表1这件事完成的时间 依次类推
        # 也就是说, 时间i完成单个事件i,所需要的时间是: time[i-1]

        self.build()  # 初始化
        # 建立图,添加边
        for u, v in relations:
            self.addChainEdge(u, v)  # u-->v 添加一条边
            self.indegree[v] += 1  # 节点v的入度++

        # 先遍历一遍,把入度为0的节点加入到队列里面
        for i in range(1, n + 1):
            if self.indegree[i] == 0:
                self.queue[self.r] = i  # 加入到r位置
                self.r += 1  # r++,队列的长度+1
        # 开始拓扑排序
        while self.l < self.r:
            cur: int = self.queue[self.l]  # 弹出入度为0的节点
            self.l += 1  # 队列头部指针++
            # cost[cur]在此之前表示,完成cur之前的课程所需要的时间 time[cur-1]:cur这个课程单点完成所需要的时间
            self.cost[cur] += time[cur - 1]  # 每一个点完成的时间先加自己的单点,更新成完成这课程以及前面的课程所需要的时间
            # 遍历cur的邻居,也就是后续的课程,给后续的课程推时间
            ei = self.head[cur]  # cur的第一条边的编号
            while ei > 0:
                v = self.to[ei]  # cur的邻居节点v
                # 这个时候 cost[v]可能已经有一个完成v之前的课程所需要的时间,现在跟我的这个 cur推的时间比
                self.cost[v] = max(self.cost[v], self.cost[cur])  # 谁更大就维持谁
                self.indegree[v] -= 1  # 邻居v的入度--
                if self.indegree[v] == 0:
                    self.queue[self.r] = v  # 把入度为0的节点加入到队列里面
                    self.r += 1  # 队列的队尾指针++,队列的长度+1
                ei = self.next[ei]  # 去下一条边

        ans: int = max(self.cost)

        return ans
