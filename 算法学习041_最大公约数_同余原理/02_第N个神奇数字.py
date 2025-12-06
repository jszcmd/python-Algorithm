"""
✨ 第 n 个神奇数字
📎 LeetCode 测试链接: https://leetcode.cn/problems/nth-magical-number/
===========================================

🎯 问题描述:
一个正整数如果能被 a 或 b 整除,那么它是神奇的.
给定三个整数 n, a, b,返回第 n 个神奇的数字.
因为答案可能很大,所以返回答案对 10^9 + 7 取模后的值.

📊 示例:

📌 示例 1:
输入: n = 1, a = 2, b = 3
输出: 2
📝 解释:神奇数字序列: 2, 3, 4, 6, 8, 9, 10, 12, ...
     第 1 个是 2 ✅

📌 示例 2:
输入: n = 4, a = 2, b = 3
输出: 6
📝 解释: 神奇数字序列: 2, 3, 4, 6, ...
     第 4 个是 6 ✅

🔍 神奇数字序列特点：
能被 a 整除：a, 2a, 3a, ...
能被 b 整除：b, 2b, 3b, ...
能被 a 且能被 b 整除：lcm(a,b), 2*lcm(a,b), ...

🧮 算法思路:
1️⃣ 计算 lcm = lcm(a, b)
2️⃣ 使用二分查找,在 [min(a,b), min(a,b)*n] 范围内搜索
3️⃣ 用容斥原理计算 [1, mid] 范围内的神奇数字个数：
   count = mid//a + mid//b - mid//lcm
4️⃣ 找到第 n 个神奇数字,对 MOD 取模

⏱️ 时间复杂度：O(log(min(a,b) * n))
💾 空间复杂度：O(1)

⚡ 难度：Hard
🏷️ 标签：数学、二分查找、容斥原理
"""


class Solution:
    # 🎯 寻找第 n 个神奇数字
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """
        :param n: 要找第几个神奇数字
        :param a: 第一个除数
        :param b: 第二个除数
        :return: 第 n 个神奇数字对 10^9 + 7 取模的结果
        """

        ans = 0  # 🔄 记录满足条件的最小值
        lcm = self.lcm(a, b)  # 🧮 计算 a 和 b 的最小公倍数
        l = 0  # 🔲 左边界
        r = n * min(a, b)  # 🔲 右边界:最坏情况是 n 乘以较小的除数

        # 🔄 二分查找开始
        while l <= r:
            m = (l + r) // 2  # 📍 中间点

            # 🧮 计算 [1, m] 范围内的神奇数字数量(容斥原理)
            count = m // a + m // b - m // lcm

            if count >= n:
                # ✅ [1, m] 范围内的神奇数字数量 ≥ n
                # 📍 记录当前 m,它可能是答案
                ans = m
                # 🔙 继续向左搜索,尝试找到更小的满足条件的值
                r = m - 1
            else:
                # ❌ [1, m] 范围内的神奇数字数量 < n
                # 🔜 需要更大的范围,向右搜索
                l = m + 1

        # 🎯 返回结果,取模防止溢出
        MOD = 10 ** 9 + 7
        return ans % MOD

    # 🧮 计算最大公约数
    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)

    # 🧮 计算最小公倍数
    def lcm(self, a: int, b: int) -> int:
        return a // self.gcd(a, b) * b
