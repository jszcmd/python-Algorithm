""" 子集 """
# 力扣测试链接:https://leetcode.cn/problems/subsets-ii/description/
# 注意提交的时候把下面的类名改成Solution

import itertools  # 导入这个库使用库函数
from typing import List


# 时间复杂度O(2^n * n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []  # 要返回的数组嵌套的数组
        nums.sort()  # 先把nums进行排序,让相同元素相邻
        path = [-1] * len(nums)  # 准备好一个等长的path数组,用于存储当前路径
        self.backtrack_groups(nums, 0, path, 0, ans)
        return ans

    # 递归生成所有不重复子集(按组处理重复元素)
    def backtrack_groups(self, nums: List[int], i: int, path: List[int], size: int, ans):
        """
        递归生成所有不重复子集(按组处理重复元素)

        :param nums: 排序好的数组，相同元素相邻
        :param i: 当前处理的起始索引位置
        :param path: 固定大小的路径数组,存储当前选择的元素
        :param size: 路径数组中有效元素的个数(填充到的位置)
        :param ans: 结果列表,收集所有不重复的子集
        """
        # 终止条件:当处理完所有元素时,将当前路径的有效部分加入结果
        if i == len(nums):
            ans.append(path[:size])  # 只复制path中[0, size-1]范围的元素
        else:
            # 步骤1：找到当前元素组的边界
            j = i + 1  # j初始化为下一个位置
            # 向右遍历,找到第一个不等于当前元素的位置(下一组的起始位置)
            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            # 情况1：不选择当前组的任何元素
            # 直接跳到下一组继续处理,size保持不变(不添加任何当前组元素)
            self.backtrack_groups(nums, j, path, size, ans)

            # 情况2:选择当前组的1个、2个...直到所有重复元素
            # 逐个添加当前组的元素,每次添加一个就递归一次
            while i < j:
                # 将当前元素添加到路径的size位置
                path[size] = nums[i]
                size += 1  # 有效元素个数增加
                # 递归处理:当前组已处理i+1个元素,跳到下一组继续
                self.backtrack_groups(nums, j, path, size, ans)
                i += 1  # 移动到当前组的下一个元素


# 时间复杂度: O(2^n * n)
class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result_set = set()

        # 获取所有长度的组合
        for length in range(len(nums) + 1):
            for combo in itertools.combinations(nums, length):
                # 排序并转换为元组以便去重
                result_set.add(tuple(sorted(combo)))

        # 将元组转换回列表
        return [list(item) for item in result_set]
