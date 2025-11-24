""" 不含重复数字的数组的所有可能的全排列 """
# 测试链接:https://leetcode.cn/problems/permutations/
# 直接把下面的Solution类复制到力扣里面

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []  # 📦 存储所有排列结果的列表
        self.backtrack(nums, 0, ans)  # 🚀 从索引0开始回溯生成排列
        return ans

    def backtrack(self, nums, i, ans):
        # 🎯 递归终止条件:当i到达数组末尾,说明一个排列已完成
        if i == len(nums):
            cur = nums[::]  # 📋 创建当前排列的深拷贝
            ans.append(cur)  # ✅ 将完整排列加入结果列表
        else:
            # 🔄 遍历从当前位置i到末尾的所有可能选择
            for j in range(i, len(nums)):
                # 🔁 交换元素:将nums[j]放到位置i
                nums[i], nums[j] = nums[j], nums[i]

                # 🎯 递归处理下一个位置
                self.backtrack(nums, i + 1, ans)  # ➡️ 深入下一层递归

                # ↩️ 回溯:恢复交换前的状态,尝试其他可能性
                nums[i], nums[j] = nums[j], nums[i]


# ⏰ 总体时间复杂度：O(n × n!)
# - n! 个排列,每个排列需要 O(n) 时间复制到结果中
# - 其中 n 为数组长度

if __name__ == '__main__':
    # 🧪 测试代码
    solution = Solution()
    nums = [1, 2, 3]  # 🔢 测试数据
    result = solution.permute(nums)  # ⚡ 执行排列生成
    print(f"输入: nums = {nums}")
    print(f"输出: {result}")
    print(f"排列数量: {len(result)}")
