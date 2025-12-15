"""
【题目】739. 每日温度
 #### 测试链接: https://leetcode.cn/problems/daily-temperatures/description/

【题目描述】
给定一个整数数组 temperatures ,表示每天的温度,返回一个数组 answer ,其中 answer[i] 是指对于第 i 天,
下一个更高温度出现在几天后,如果气温在这之后都不会升高,请在该位置用 0 来代替.

【示例 1】
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

【示例 2】
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

【示例 3】
输入: temperatures = [30,60,90]
输出: [1,1,0]

【提示】
* 1 <= temperatures.length <= 10^5
* 30 <= temperatures[i] <= 100
"""

from typing import List

class Solution:
    # 使用固定长度数组模拟栈,避免 append/pop 的动态扩容开销
    # 根据题目提示,数据范围最大为 10^5
    stack: list[int] = [0] * 100001
    r: int = 0  # 栈顶指针

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n: int = len(temperatures)
        ans: list[int] = [0] * n  # 结果数组初始化为0
        cur: int = 0
        
        # 每次调用前重置栈指针
        self.r = 0 

        for i in range(n):
            # 单调栈逻辑:保持栈内温度递减
            # 如果当前温度 > 栈顶温度,说明栈顶那天找到了升温日
            while (self.r > 0 and temperatures[self.stack[self.r - 1]] < temperatures[i]):
                cur = self.stack[self.r - 1] # 取出栈顶那一天的下标
                self.r -= 1                  # 弹出
                ans[cur] = i - cur           # 计算天数差
            
            # 当前天入栈等待
            self.stack[self.r] = i
            self.r += 1

        return ans