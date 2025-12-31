# ======================================================================================
# 题目: P4017 最大食物链计数
# 来源: 洛谷 (Luogu)
# #### 测试连接: https://www.luogu.com.cn/problem/P4017
#
# 题目描述:
# 给你一个食物网，你要求出这个食物网中最大食物链的数量。
# (这里的"最大食物链", 指的是生物学意义上的食物链, 即最左端是不会捕食其他生物的生产者,
# 最右端是不会被其他生物捕食的消费者.)
#
# 由于这个结果可能过大, 你只需要输出总数模上 80112002 的结果.
#
# 输入格式:
# 第一行, 两个正整数 n、m, 表示生物种类 n 和吃与被吃的关系数 m.
# 接下来 m 行，每行两个正整数 A B, 表示被吃的生物 A 和吃 A 的生物 B (即存在边 A -> B)。
#
# 输出格式:
# 一行一个整数, 为最大食物链数量模上 80112002 的结果.
#
# 数据范围:
# 1 <= n <= 5000
# 1 <= m <= 500000
# 保证图中不会出现环(DAG).
# ======================================================================================

import sys
from collections import deque


def ways():
    MOD: int = 80112002
    # 一次性读入所有的数据,并以空格分割,input_data此时是一个列表
    input_data = sys.stdin.read().split()
    if not input_data: return 0  # 没有输入任何数据,直接返回
    # 把读入的数据转成可迭代对象,方便获取数据
    iterator = iter(input_data)

    try:
        n = int(next(iterator))  # 读入节点数n
        m = int(next(iterator))  # 读入边的数量m
    except StopIteration:
        return 0  # 当要读入的迭代器没有数据,直接退出

    # 邻接表建图 : adjList[u] : 表示节点u指向的所有节点
    adjList = [[] for _ in range(n + 1)]  # 0位置不用
    # 入度表: indegree[i] 表示有多少条边指向节点i
    indegree = [0] * (n + 1)  # 0位置也不用
    # 向上推送的信息,默认初始化为0
    lines = [0] * (n + 1)  # 0位置也不使用
    # 拓扑排序需要的队列
    queue = deque()

    # 建图,添加这m条边
    for _ in range(m):
        u = int(next(iterator))  # 起点
        v = int(next(iterator))  # 终点
        adjList[u].append(v)  # u-->v建一条边
        indegree[v] += 1  # 节点v的入度++

    # 先把入度为0的节点加入到队列
    for i in range(1, n + 1):  # 从节点1开始
        if indegree[i] == 0:
            queue.append(i)  # 把入度为0的点加入到队列里面
            lines[i] = 1  # 最开始入度为0的消息设置为1

    ans: int = 0  # 要返回的答案

    # 开始拓扑排序
    while queue:
        cur = queue.popleft()  # 弹出最左边的元素(入度为0的节点)

        if len(adjList[cur]) == 0:  # 当前弹出的节点不在有任何邻居了
            ans = (ans + lines[cur]) % MOD
        else:  # 当前弹出的节点还有邻居
            for v in adjList[cur]:  # 遍历cur的所有邻居v
                lines[v] = (lines[cur] + lines[v]) % MOD  # 把u的路径加入到v上面去
                indegree[v] -= 1  # v的入度--
                if indegree[v] == 0: queue.append(v)  # 把入度为0的邻居加入到队列里面

    return ans


if __name__ == '__main__':
    print(ways())
