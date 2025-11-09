""" 字符串的全部子序列(填函数风格) """
# 牛客测试链接:https://www.nowcoder.com/practice/92e6247998294f2c933906fdedbc6e6a
# 提交的时候把下面的类名改成Solution
# 代码中的类名、方法名、参数名已经指定,请勿修改,直接返回方法规定的值即可
# 下面两种方法的时间复杂度: O(2^n * n)
from typing import List

""" 使用动态数组+回溯实现 """


class Solution1:
    def generatePermutation(self, s: str) -> List[str]:
        """
        :param s: 目标字符串
        :return: 返回值字符数组
        """
        result_set = set()  # 集合,收集结果时去重
        path = []  # 准备好一个路径数组
        self.backtrack(s, 0, path, result_set)
        return list(result_set)

    # 使用动态数组的回溯递归(result_set就不要限制类型了,知道它是一个集合就可以了)
    def backtrack(self, s: str, i: int, path: List[str], result_set) -> None:
        """
        :param s: 目标字符串
        :param i: 处理的字符串中索引为i的位置
        :param path: 之前决定的路径
        :param result_set: 收集结果时去重
        :return: 无返回值,对全局变量path和result_set进行修改
        """
        if i == len(s):
            result_set.add(''.join(path))  # 将路径转换为字符串并加入集合
        else:
            # 路径(1):选择当前字符
            path.append(s[i])  # ✅ 选择:加上当前字符
            self.backtrack(s, i + 1, path, result_set)  # 递归处理下一个字符
            path.pop()  # ↩️ 回溯:撤销选择
            """ 把加进去的字符删除掉,走另一条路径 """
            # 路径(2):不选择当前字符
            self.backtrack(s, i + 1, path, result_set)  # ❌ 不选择:直接处理下一个字符


""" 使用固定数组+数组的复用实现 """


class Solution2:
    def generatePermutation(self, s: str) -> List[str]:
        """
        :param s: 目标字符串
        :return: 返回值字符数组
        """
        result_set = set()
        path = [''] * len(s)  # 准备好一个长度为len(s)的字符数组
        self.backtrack_fixed(s, 0, path, 0, result_set)
        return list(result_set)

    # 使用固定大小路径数组的递归函数
    def backtrack_fixed(self, s, i: int, path: List[str], size: int, result_set):
        """
        :param s: 原始字符串
        :param i: 当前处理的索引
        :param path: 固定大小的路径数组
        :param size: 用size表示路径中填了几个有效字符
        :param result_set: 结果集合
        :return: 无返回值,对全局变量path和result_set进行修改
        """
        # 将路径中前size个字符转换为字符串
        if i == len(s):
            result_set.add(''.join(path[:size]))
        else:
            # 选择当前字符:放入路径的size位置
            path[size] = s[i]
            self.backtrack_fixed(s, i + 1, path, size + 1, result_set)

            # 不选择当前字符:size保持不变
            self.backtrack_fixed(s, i + 1, path, size, result_set)
