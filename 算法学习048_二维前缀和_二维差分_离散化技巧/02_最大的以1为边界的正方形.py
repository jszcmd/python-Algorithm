"""
=================================================================================
1139. 最大的以 1 为边界的正方形
### 测试链接: https://leetcode.cn/problems/largest-1-bordered-square/description/

* 给你一个由若干 0 和 1 组成的二维网格 grid,请你找出边界全部由 1 组成的最大 正方形
子网格，并返回该子网格中的元素数量。如果不存在,则返回 0。

* 示例 1:
输入:grid = [[1,1,1],[1,0,1],[1,1,1]]
输出:9

* 示例 2:
输入:grid = [[1,1,0,0]]
输出:1

* 提示：
1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1
=================================================================================
"""

from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        
        # 1. 预处理:原地构建二维前缀和
        self.bulid(grid, m, n)
        
        # 2. 特判:如果矩阵总和为0,说明全是0,返回0
        if (self.get_sum(grid, 0, 0, m-1, n-1) == 0):
            return 0
            
        ans: int = 1 # 记录最大边长,至少为1

        # 3. 枚举左上角 (a, b)
        for a in range(m):
            for b in range(n):
                # 4. 剪枝:直接从比当前 ans 大一圈的尺寸开始尝试
                c = a + ans    # 右下角行
                d = b + ans    # 右下角列
                k = ans + 1    # 当前尝试的边长
                
                # 只要不越界，就尝试更大的正方形
                while (c < m and d < n): 
                    # 5. 核心公式：大正方形面积 - 内部小正方形面积 == 边框理论面积
                    # (k-1)<<2 等价于 (k-1)*4，即周长
                    if self.get_sum(grid,a,b,c,d) - self.get_sum(grid,a+1,b+1,c-1,d-1) == (k-1)<<2:
                        ans = k # 更新最大边长
                    
                    # 继续扩大一圈尝试
                    c += 1
                    d += 1
                    k += 1
        return ans * ans

    # 构造前缀和:grid[i][j] = 上 + 左 - 左上 + 原值
    def bulid(self, grid, m, n):
        for i in range(m):
            for j in range(n):
                grid[i][j] += self.get(grid,i,j-1) + self.get(grid,i-1,j) - self.get(grid,i-1,j-1)

    # 容斥原理求子区域和:右下 - 左半 - 上半 + 左上重叠
    def get_sum(self, sum_arr, a, b, c, d):
        if a > c: # 处理 k=1 时内部矩形坐标交叉的情况
            return 0
        else:
            return self.get(sum_arr,c,d) - self.get(sum_arr,c,b-1) - self.get(sum_arr,a-1,d) + self.get(sum_arr,a-1,b-1)
    
    # 安全访问:越界返回 0
    def get(self, sum_arr, i, j):
        if i < 0 or j < 0:
            return 0
        else:
            return sum_arr[i][j]
