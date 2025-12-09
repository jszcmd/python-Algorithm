""" 航班预定统计:力扣测试 """
# 力扣测试链接:https://leetcode.cn/problems/corporate-flight-bookings/

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 🛡️ Step 1: 初始化差分数组 (防越界)
        # ------------------------------------------------------
        # 申请 n + 2 的空间，是为了处理 "last + 1" 可能等于 n + 1 的情况。
        # 这样我们可以放心地操作下标，不用每次都判断边界。
        cnt = [0] * (n + 2)

        # 🎫 Step 2: 构建差分记录 (核心逻辑)
        # ------------------------------------------------------
        # 遍历每一条预订记录：[开始航班, 结束航班, 座位数]
        for first, last, seats in bookings:
            # 🛫【登机】：在区间起点 first
            # 意味着从这里开始，飞机上增加了 seats 个预订
            cnt[first] += seats

            # 🛬【下机】：在区间终点的下一位 last + 1
            # 意味着预订结束，需要减去 seats 以抵消之前的增加
            cnt[last + 1] -= seats

        # 🌊 Step 3: 加工前缀和 (还原真实数据)
        # ------------------------------------------------------
        # 差分数组记录的是“变化量”，前缀和能将其还原为“总量”。
        # 我们就像滚雪球一样，把之前的变化累加到当前。
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i - 1]

        # 🎁 Step 4: 导出结果
        # ------------------------------------------------------
        # 题目只要 n 个航班的数据 (下标 1 到 n)
        # 利用切片直接截取有效区间返回
        return cnt[1: n + 1]
