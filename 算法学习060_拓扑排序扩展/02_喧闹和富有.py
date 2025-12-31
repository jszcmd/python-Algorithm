# ======================================================================================
# 题目: 851. 喧闹和富有 (Loud and Rich)
# 来源: LeetCode
# #### 测试链接: https://leetcode.cn/problems/loud-and-rich/description/
#
# 题目描述:
# 有一组 n 个人作为实验对象, 从 0 到 n - 1 编号, 其中每个人都有不同数目的钱,
# 以及不同程度的安静值 (quietness).
#
# 给你一个数组 richer，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱.
# 另给你一个整数数组 quiet, 其中 quiet[i] 是 person i 的安静值.
# richer 中所给出的数据 逻辑自洽 (也就是说, 在 person x 比 person y 更有钱的同时,
# 不会出现 person y 比 person x 更有钱的情况 ).
#
# 现在, 返回一个整数数组 answer 作为答案, 其中 answer[x] = y 的前提是:
# 在所有拥有的钱肯定不少于 person x 的人中，person y 是最安静的人(也就是安静值 quiet[y] 最小的人).
#
# 示例 1:
# 输入: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
# 输出: [5,5,2,5,4,5,6,7]
#
# 提示:
# n == quiet.length
# 1 <= n <= 500
# 0 <= quiet[i] < n
# quiet 的所有值 互不相同
# 0 <= richer.length <= n * (n - 1) / 2
# ======================================================================================

from collections import deque
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)  # 安静数组的长度,也是节点的个数
        # 邻接表建图 : adjList[u] : 表示节点u指向的所有节点
        adjList = [[] for _ in range(n)]  # 0位置的也使用
        # 入度表: indegree[i] 表示有多少条边指向节点i
        indegree = [0] * n  #
        # 拓扑排序需要的队列
        queue = deque()
        # 安静数组(要返回的), ans[x]:比x有钱且比x安静的
        ans = [x for x in range(n)]  # 最开始每个人最安静的人默认是自己

        # 添加边,建图
        for u, v in richer:
            adjList[u].append(v)  # u-->v 添加一条边
            indegree[v] += 1  # 节点v的入度++

        # 把入度为0的加入到队列里面
        for i in range(n):
            if indegree[i] == 0: queue.append(i)  # 发现入度为0的节点加入到队列

        while queue:
            cur = queue.popleft()  # 弹出入度为0的节点
            for v in adjList[cur]:  # 遍历cur的邻居v,cur是比v都更加富有的
                # 发现cur已经知道的且比cur安静的 比 v已知的且比v安静的还要安静
                if quiet[ans[cur]] < quiet[ans[v]]: ans[v] = ans[cur]  # 更行v的安静数组
                indegree[v] -= 1  # cur的邻居的入度--
                if indegree[v] == 0: queue.append(v)  # 发现入度为0的点加入到队列

        return ans
