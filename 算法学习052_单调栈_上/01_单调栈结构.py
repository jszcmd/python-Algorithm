"""
### 测试链接: https://www.nowcoder.com/practice/2a2c00e7a88a498693568cef63a4b7bb
【题目描述】
给定数组 arr,找到每个位置 i 左右两边最近且值比 arr[i] 小的位置下标.

【输入输出】
输入:第一行长度 n,第二行 n 个整数.
输出:n 行,每行两个数 L R (不存在记 -1).

【数据范围】
1 <= n <= 1000000
----------------------------------------------------------------
"""

import sys


# --- 核心逻辑 ---
def compute():
    # 声明使用全局变量 r (栈指针) 和 n (数组长度)
    global r, n
    r = 0  # 栈指针初始化:r=0 表示栈为空
    cur: int = 0

    # ==========================
    # 阶段 1: 遍历数组 (核心单调栈逻辑)
    # ==========================
    for i in range(n):
        # 当栈不为空 且 栈顶元素 >= 当前元素
        # 说明 arr[i] 是栈顶元素右边遇到的第一个"更小或相等"的值
        while r > 0 and arr[stack[r - 1]] >= arr[i]:
            cur = stack[r - 1]  # 获取要弹出的栈顶元素下标
            r -= 1  # 弹出

            # 【记录左边答案】:剩下的栈顶就是左边第一个比它小的
            ans[cur][0] = stack[r - 1] if r > 0 else -1

            # 【记录右边答案】: i 是让 cur 弹出的数
            # 注意:题目要求"值比 arr[i] 小",如果这里是相等,会在阶段3修正
            ans[cur][1] = i

        # 当前位置入栈
        stack[r] = i
        r += 1

    # ==========================
    # 阶段 2: 清算阶段 (处理栈中剩余元素)
    # ==========================
    while r > 0:
        cur = stack[r - 1]
        r -= 1
        ans[cur][0] = stack[r - 1] if r > 0 else -1
        # 还在栈里说明右边没有比它小的数了
        ans[cur][1] = -1

    # ==========================
    # 阶段 3: 修正阶段 (处理重复值)
    # ==========================
    # 题目明确提到"可能有重复值"且要求找"比 arr[i] 小"的位置。
    # 如果 ans[i][1] 位置的值和 arr[i] 相等,说明它不是严格小于,需要继续向右找.
    for i in range(n - 2, -1, -1):
        if ans[i][1] != -1 and arr[ans[i][1]] == arr[i]:
            ans[i][1] = ans[ans[i][1]][1]


# --- 极速输入输出优化 ---
if __name__ == '__main__':
    # 1. 极速输入:一次性读入所有内容 (解决大量数据输入的超时问题)
    input_data = sys.stdin.read().split()

    if input_data:
        # 使用迭代器顺序获取数据
        iterator = iter(input_data)

        # 提取 n
        n = int(next(iterator))

        # 提取 arr (列表推导式生成数组)
        arr = [int(next(iterator)) for _ in range(n)]

        # 初始化全局变量
        stack = [0] * n  # 模拟栈
        ans = [[0, 0] for _ in range(n)]  # 结果数组
        r = 0  # 栈顶指针

        # 执行核心逻辑
        compute()

        # 2. 极速输出:拼接字符串一次性打印 (解决大量数据输出的超时问题)
        sys.stdout.write('\n'.join([f"{row[0]} {row[1]}" for row in ans]))
        sys.stdout.write('\n')
