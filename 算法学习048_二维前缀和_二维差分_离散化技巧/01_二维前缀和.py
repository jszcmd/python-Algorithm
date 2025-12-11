"""
=================================================================================
304. 二维区域和检索 - 矩阵不可变 (Range Sum Query 2D - Immutable)
### 测试链接: https://leetcode.cn/problems/range-sum-query-2d-immutable/description/

* 通俗题目描述:
给你一个由数字组成的二维矩阵 matrix。
你需要实现一个功能,能够快速计算出矩阵中任意一个"子矩形"范围内所有数字的总和.

* 输入告诉我们：
1. 这是一个"不可变"的矩阵(初始化后,里面的数字不会变).
2. 会有多次查询请求(sumRegion),所以每次都暴力遍历去加会超时,必须预处理.

* 查询参数:
给定左上角 (row1, col1) 和 右下角 (row2, col2),返回这块区域的和.

* 示例:
输入矩阵:
[
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

查询 sumRegion(2, 1, 4, 3) -> 返回红色矩形框的和 -> 8
查询 sumRegion(1, 1, 2, 2) -> 返回绿色矩形框的和 -> 11
查询 sumRegion(1, 2, 2, 4) -> 返回蓝色矩形框的和 -> 12
=================================================================================
"""

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m: int = len(matrix)                            # 获取行数 m
        n: int = len(matrix[0])                         # 获取列数 n
        
        # 初始化 (m+1)*(n+1) 的数组，第 0 行和第 0 列作为哨兵自动初始化为 0
        self.sum_arr: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 1. 数据搬运:将 matrix 填入 sum_arr,索引整体向右下偏移 1 位
        for i in range(m):
            for j in range(n):
                self.sum_arr[i+1][j+1] = matrix[i][j]   # 原矩阵(0-based) -> 前缀和数组(1-based)
        
        # 2. 核心计算:原地累加计算二维前缀和
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 公式:当前格 = 左边 + 上边 - 左上角重叠部分 + 本身数值(已填入)
                self.sum_arr[i][j] += self.sum_arr[i][j-1] + self.sum_arr[i-1][j] - self.sum_arr[i-1][j-1]

    # 参数说明：a,b 是左上角(row1, col1)，c,d 是右下角(row2, col2)
    def sumRegion(self, a: int, b: int, c: int, d: int) -> int:
        # 坐标映射:输入题目给的是 0-based,内部计算用 1-based
        a += 1  # 左上角行 row1
        b += 1  # 左上角列 col1
        c += 1  # 右下角行 row2
        d += 1  # 右下角列 col2
        
        # 容斥原理：大矩形(右下) - 上半部 - 左半部 + 多减去的左上重叠部分
        return self.sum_arr[c][d] - self.sum_arr[c][b-1] - self.sum_arr[a-1][d] + self.sum_arr[a-1][b-1]
    
