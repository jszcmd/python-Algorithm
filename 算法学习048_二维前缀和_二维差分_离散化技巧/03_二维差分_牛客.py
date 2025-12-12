"""
======================================================================================
题目: 矩阵子区域更新 (二维差分模板题)
测试链接: https://www.nowcoder.com/practice/50e1a93989df42efb0b1dec386fb4ccc

【题目描述】
给定一个 n * m 的整数矩阵 origin, 下标从 1 开始.
需要执行 q 次操作.
每次操作给定 5 个整数 x1, y1, x2, y2, k.
表示将以 (x1, y1) 为左上角、(x2, y2) 为右下角的子矩阵内所有元素增加 k.
(k 可以是负数, 表示减少)
请输出所有操作执行完毕后的最终矩阵.

【数据范围】
1 <= n, m <= 1000
1 <= q <= 100000
-10^9 <= 初始数值, k <= 10^9 
(注: Python 的 int 会自动处理大整数,无需像 C 语言那样担心 int 溢出或强制使用 long long)
======================================================================================
"""

import sys

# 【配置】最大矩阵尺寸
# 题目通常 N <= 1000,设置为 1002 是为了预留边界(padding),防止下标越界
MAX = 1002

# 【原始矩阵】存放输入的初始数值
origin = [[0] * MAX for _ in range(MAX)]

# 【差分数组】存放变化量
# diff[i][j] 的值经过前缀和计算后,表示 (i,j) 位置累积增加/减少的数值
diff = [[0] * MAX for _ in range(MAX)]

n = 0 # n行
m = 0 # m列
q = 0 # 操作q次

# 【核心算法 1】二维差分更新
# 时间复杂度: O(1)
# 原理: 修改四个关键点,即可达成矩形区域内的整体增减
def add(a, b, c, d, v):
    diff[a][b] += v             # 左上角: 开始增加
    diff[c + 1][b] -= v         # 右上角右侧: 消除横向影响
    diff[a][d + 1] -= v         # 左下角下方: 消除纵向影响
    diff[c + 1][d + 1] += v     # 右下角右下方: 补回重复减去的部分

# 【核心算法 2】二维前缀和构建
# 时间复杂度: O(nm)
# 原理: 将差分标记还原为每个位置实际的累积变化量
def build():
    # 注意 range 是左闭右开,循环范围是 1 到 n
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 递推公式: 当前值 = 左 + 上 - 左上 + 差分标记
            diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]

if __name__ == '__main__':
    # 【性能优化】快速 I/O
    # sys.stdin.read().split() 一次性读入所有数据到内存,比 input() 快几十倍
    # 能够有效防止因读取大量数据导致的超时 (TLE)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        sys.exit(0)
    
    # 创建迭代器,用于顺序获取每一个整数
    iterator = iter(input_data)

    try:
        # 1. 读取 n(行), m(列), q(操作次数)
        n = int(next(iterator))
        m = int(next(iterator))
        q = int(next(iterator))

        # 2. 读取原始矩阵数据
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                origin[i][j] = int(next(iterator))

        # 3. 处理 q 次差分操作
        for _ in range(q):
            a = int(next(iterator))
            b = int(next(iterator))
            c = int(next(iterator))
            d = int(next(iterator))
            v = int(next(iterator))
            add(a, b, c, d, v)

    except StopIteration:
        pass

    # 4. 执行前缀和计算,还原 diff 数组
    build()

    # 【性能优化】快速输出
    # 频繁调用 print() 极其耗时,先将结果存入列表
    output_buffer = []
    for i in range(1, n + 1):
        # 1. 预分配长度为 m+1 的数组
        row_str = ['0'] * (m + 1)
        for j in range(1, m + 1):
            # 计算最终值
            val = origin[i][j] + diff[i][j]
            # 2. 【关键】必须转为字符串并赋值给对应下标
            row_str[j] = str(val)
        # 3. 【关键】使用切片 row_str[1:] 忽略掉下标 0 的占位符
        output_buffer.append(" ".join(row_str[1:]))
    
    # 最后用换行符拼接所有行,一次性输出
    sys.stdout.write("\n".join(output_buffer) + "\n")

