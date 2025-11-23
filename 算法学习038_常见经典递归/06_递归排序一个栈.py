from collections import deque


class Solution:
    def stack_sort(self, stack: deque) -> None:
        """
        🎯 栈排序算法 - 递归选择排序
        📌 通过递归找到最大值并下沉到栈底,实现栈的排序
        """
        depth: int = self.deep(stack)  # 🔍 计算栈的深度
        while depth > 0:
            # 🔍 找到前depth个元素中的最大值
            max_num = self.depth_max(stack, depth)
            # 🔢 统计最大值在前depth个元素中出现的次数
            k: int = self.times(stack, depth, max_num)
            # 🔽 将最大值下沉到栈底
            self.down(stack, depth, max_num, k)
            # 📉 减少待处理深度，排除已排序的最大值
            depth -= k

    def deep(self, stack: deque) -> int:
        """
        📏 计算栈的深度（不改变栈的数据顺序）
        📌 通过递归弹出并重新压入的方式计算栈中元素个数
        """
        if not stack:
            return 0  # 🛑 基准情况：空栈深度为0

        num: int = stack.pop()  # 🎯 弹出栈顶元素
        depth: int = self.deep(stack) + 1  # 🔄 递归计算剩余栈的深度并加1
        stack.append(num)  # 🔼 恢复弹出的元素，保持栈原样
        return depth

    def depth_max(self, stack: deque, depth: int) -> int:
        """
        🔍 查找栈中前depth个元素的最大值
        📌 递归遍历栈的前depth个元素，找到其中的最大值
        """
        if depth == 0:
            return -2147483648  # 🚫 基准情况：深度为0时返回最小值

        num: int = stack.pop()  # 🎯 弹出栈顶元素
        rest_max: int = self.depth_max(stack, depth - 1)  # 🔄 递归查找剩余元素的最大值
        max_num = max(num, rest_max)  # ⚡ 比较当前元素与剩余最大值
        stack.append(num)  # 🔼 恢复弹出的元素
        return max_num

    def times(self, stack: deque, depth: int, max_num: int) -> int:
        """
        🔢 统计栈中前depth个元素中最大值出现的次数
        📌 递归遍历前depth个元素，统计目标最大值出现的次数
        """
        if depth == 0:
            return 0  # 🛑 基准情况：深度为0时返回0次

        num: int = stack.pop()  # 🎯 弹出栈顶元素
        rest_times: int = self.times(stack, depth - 1, max_num)  # 🔄 递归统计剩余元素
        times: int = rest_times + (1 if num == max_num else 0)  # ➕ 当前元素匹配则计数+1
        stack.append(num)  # 🔼 恢复弹出的元素
        return times

    def down(self, stack: deque, depth: int, max_num: int, k: int) -> None:
        """
        🔽 将栈中前depth个元素中的最大值下沉到指定位置
        📌 关键步骤：将最大值移动到栈的底部（已排序区域）
        """
        if depth == 0:
            # 🎯 基准情况：处理完所有元素后，在栈底压入k个最大值
            for i in range(k):
                stack.append(max_num)  # 🔼 压入最大值到栈底
        else:
            num: int = stack.pop()  # 🎯 弹出栈顶元素
            self.down(stack, depth - 1, max_num, k)  # 🔄 递归处理剩余元素

            if num != max_num:
                stack.append(num)  # 🔼 如果不是最大值，重新压回栈中
            # 💡 如果是最大值，就不压回，相当于将其"过滤"掉


def test_stack_sort():
    """
    🧪 测试栈排序功能
    """
    sol = Solution()

    # 🧪 测试用例1: 乱序数组
    stack1 = deque([3, 1, 4, 2])
    print(f"📥 原始栈: {list(stack1)}")
    sol.stack_sort(stack1)
    print(f"📤 排序后: {list(stack1)}")
    print("🎯 期望: [1, 2, 3, 4] (升序)")
    print("---")

    # 🧪 测试用例2: 已排序数组
    stack2 = deque([1, 2, 3, 4])
    print(f"📥 原始栈: {list(stack2)}")
    sol.stack_sort(stack2)
    print(f"📤 排序后: {list(stack2)}")
    print("---")

    # 🧪 测试用例3: 逆序数组
    stack3 = deque([4, 3, 2, 1])
    print(f"📥 原始栈: {list(stack3)}")
    sol.stack_sort(stack3)
    print(f"📤 排序后: {list(stack3)}")
    print("---")

    # 🧪 测试用例4: 包含重复元素
    stack4 = deque([2, 2, 1, 3, 2])
    print(f"📥 原始栈: {list(stack4)}")
    sol.stack_sort(stack4)
    print(f"📤 排序后: {list(stack4)}")
    print("🎯 期望: [1, 2, 2, 2, 3]")
    print("---")

    # 🧪 测试用例5: 空栈
    stack5 = deque()
    print(f"📥 原始栈: {list(stack5)}")
    sol.stack_sort(stack5)
    print(f"📤 排序后: {list(stack5)}")
    print("---")


if __name__ == "__main__":
    # 🚀 运行测试
    test_stack_sort()
