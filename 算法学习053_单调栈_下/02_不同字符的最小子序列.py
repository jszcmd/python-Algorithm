"""
================================================================================
📘 题目: 不同字符的最小子序列 (Smallest Subsequence of Distinct Characters)
#### 🔗 题目链接: https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/
================================================================================
难度:中等
标签:栈, 贪心, 字符串, 单调栈

【题目描述】
返回 s 字典序最小的子序列,该子序列包含 s 的所有不同字符,且只包含一次.

--------------------------------------------------------------------------------
🌟 示例 1:
   输入:s = "bcabc"
   输出:"abc"

🌟 示例 2:
   输入:s = "cbacdcbc"
   输出:"acdb"

--------------------------------------------------------------------------------
📏 提示 (Constraints):
   • 1 <= s.length <= 1000
   • s 由小写英文字母组成
================================================================================
"""


class Solution:
    cnts: list[int] = [0] * 26  # 类变量:存储每种字符的剩余出现次数
    enter: list[bool] = [0] * 26  # 类变量:标记每种字符当前是否在栈中
    stack: list[str] = ['0'] * 26  # 类变量:模拟单调栈(字符集大小仅26)
    r = 0  # 类变量:栈顶指针,指向下一个写入位置

    def smallestSubsequence(self, s: str) -> str:
        self.r = 0  # 初始化栈指针,相当于清空栈

        # 必须在函数内重置,防止 LeetCode 多组测试数据间互相干扰
        self.cnts = [0] * 26  # 重置计数数组
        self.enter = [False] * 26  # 重置进栈标记

        # --- 第一步:统计词频 ---
        for char in s:  # 遍历字符串中的每个字符
            # Python不支持字符直接相减,必须用 ord() 转成 ASCII 码计算索引
            self.cnts[ord(char) - ord('a')] += 1  # 对应字符的计数 +1

        # --- 第二步:单调栈构建 ---
        # 从左往右依次遍历字符串 s,当前字符记为 cur
        for cur in s:
            # 计算当前字符 cur 对应的数组下标 (0-25)
            cur_idx = ord(cur) - ord('a')  # 这一步是为了方便查表

            # 只有当字符【不】在栈中时,我们才考虑是否将其入栈
            # 如果已经在栈中,说明之前已经保留了该字符,跳过即可(保证去重)
            if not self.enter[cur_idx]:

                # 🔥 核心逻辑:维护单调递增栈
                # 循环检查并弹出栈顶元素的条件(需同时满足):
                # 1. self.r > 0: 栈不能为空
                # 2. self.stack[...] > cur: 栈顶字符比当前字符大(字典序大,说明栈顶该让位)
                # 3. self.cnts[...] > 0: 栈顶字符在后面还会出现(如果后面没了,千万不能弹,弹了就丢了)
                while self.r > 0 and self.stack[self.r - 1] > cur and self.cnts[ord(self.stack[self.r - 1]) - ord('a')] > 0:
                    # 取出栈顶字符的索引,准备修改它的状态
                    top_idx = ord(self.stack[self.r - 1]) - ord('a')  # 计算栈顶索引
                    self.enter[top_idx] = False  # 将栈顶字符标记为"未进栈"
                    self.r -= 1  # 指针回退,相当于物理弹出栈顶元素

                # 经过 while 循环的清理后,当前位置安全了,让 cur 入栈
                self.stack[self.r] = cur  # 将当前字符写入栈顶位置
                self.r += 1  # 栈指针后移一位
                self.enter[cur_idx] = True  # 标记当前字符 cur 已经进栈

            # ⚠️ 关键点:无论当前字符是否进栈,它都已经被遍历过了
            # 所以它的"剩余出现次数"必须减 1
            self.cnts[cur_idx] -= 1

            # 截取栈中有效的部分(0 到 r),拼接成字符串返回
        return ''.join(self.stack[0:self.r])

