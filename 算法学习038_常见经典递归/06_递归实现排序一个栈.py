# 为了方便,我们就使用python中collections包中的栈,来实现栈
from collections import deque


# 这个类,也是只能排序,类型deque的栈(deque的实例化对象),当然这个是可以改的
class Solution:
    def reverse(self, stack: deque) -> None:
        """
        🎯 栈排序算法（升序排序）
        🔄 通过递归将栈元素按升序排列（栈底最小，栈顶最大）
        """
        depth: int = self.deep(stack)  # 📏 获取栈的当前深度
        while depth > 0:
            # 🔍 找到前depth个元素中的最大值
            max_num = self.depth_max(stack, depth)
            # 🎰 计算最大值在前depth个元素中出现的次数
            k: int = self.times(stack, depth, max_num)
            # ⬇️ 将最大值沉底k次
            self.down(stack, depth, max_num, k)
            # 📉 减少处理深度，跳过已处理的最大值
            depth -= k

    # 📏 返回栈的深度
    # 💡 不改变栈的数据状况 - 使用递归临时弹出再压回
    def deep(self, stack: deque) -> int:
        """
        📊 计算栈的深度（递归实现）
        """
        if not stack:
            return 0  # 🎯 基准情况：空栈深度为0

        num: int = stack.pop()  # 🎪 弹出栈顶元素
        depth: int = self.deep(stack) + 1  # 📈 递归计算剩余深度并加1
        stack.append(num)  # 🔄 恢复栈的原始状态
        return depth

    # 🔍 返回栈前depth个元素的最大值
    def depth_max(self, stack: deque, depth: int) -> int:
        """
        🏆 在栈的前depth个元素中查找最大值
        """
        if depth == 0:
            return -2147483648  # 🚫 基准情况：返回int最小值

        num: int = stack.pop()  # 🎪 弹出当前元素
        rest_max: int = self.depth_max(stack, depth - 1)  # 🔄 递归查找剩余元素的最大值
        max_num = max(num, rest_max)  # 🏅 比较当前元素和剩余元素的最大值
        stack.append(num)  # 🔄 恢复栈的原始状态
        return max_num

    # 🎰 计算最大值max_num在栈前depth个元素中出现的次数
    def times(self, stack: deque, depth: int, max_num: int) -> int:
        """
        🔢 统计最大值出现的次数
        """
        if depth == 0:
            return 0  # 🚫 基准情况：深度为0时计数为0

        num: int = stack.pop()  # 🎪 弹出当前元素
        rest_times: int = self.times(stack, depth - 1, max_num)  # 🔄 递归统计剩余元素的次数
        times: int = rest_times + (1 if num == max_num else 0)  # ➕ 如果当前元素等于最大值则计数加1
        stack.append(num)  # 🔄 恢复栈的原始状态
        return times

    # ⬇️ 将最大值沉底操作
    def down(self, stack: deque, depth: int, max_num: int, k: int) -> None:
        """
        ⏬ 将最大值沉到栈底（排序关键步骤）
        🎯 处理前depth个元素，移除所有最大值，最后在底部添加k个最大值
        """
        if depth == 0:
            # 🎯 基准情况：处理完所有元素，在底部添加k个最大值
            for i in range(k):
                stack.append(max_num)  # ➕ 在栈底添加最大值（排序后的位置）
        else:
            num: int = stack.pop()  # 🎪 弹出当前元素
            self.down(stack, depth - 1, max_num, k)  # 🔄 递归处理剩余元素

            if num != max_num:
                stack.append(num)  # 🔄 如果不是最大值，压回栈中
            # 💡 如果是最大值，不压回 - 实现"沉底"效果


# 🧪 测试排序功能
def test_stack_sort():
    """
    ✅ 测试栈排序功能
    """
    sol = Solution()

    # 🎯 测试用例1:乱序栈
    stack1 = deque([3, 1, 4, 2])
    print(f"📥 原栈: {list(stack1)}")
    sol.reverse(stack1)
    print(f"✅ 排序后: {list(stack1)}")
    print("🎯 期望: [1, 2, 3, 4] (栈底->栈顶)")
    print("---")

    # 🎯 测试用例2:已排序栈
    stack2 = deque([1, 2, 3, 4])
    print(f"📥 原栈: {list(stack2)}")
    sol.reverse(stack2)
    print(f"✅ 排序后: {list(stack2)}")
    print("---")

    # 🎯 测试用例3:逆序栈
    stack3 = deque([4, 3, 2, 1])
    print(f"📥 原栈: {list(stack3)}")
    sol.reverse(stack3)
    print(f"✅ 排序后: {list(stack3)}")
    print("---")

    # 🎯 测试用例4:有重复元素的栈
    stack4 = deque([2, 2, 1, 3, 2])
    print(f"📥 原栈: {list(stack4)}")
    sol.reverse(stack4)
    print(f"✅ 排序后: {list(stack4)}")
    print("🎯 期望: [1, 2, 2, 2, 3]")
    print("---")

    # 🎯 测试用例5:空栈
    stack5 = deque()
    print(f"📥 原栈: {list(stack5)}")
    sol.reverse(stack5)
    print(f"✅ 排序后: {list(stack5)}")
    print("---")


if __name__ == "__main__":
    # 🚀 运行测试
    test_stack_sort()
