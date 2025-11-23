# 导入queue模块中的LifoQueue
# 🔒 线程安全的栈(支持多线程)
from queue import LifoQueue


class Solution:
    def reverse(self, stack: LifoQueue) -> None:
        """
        🔄 递归反转栈中元素
        🎯 将栈底元素移动到栈顶,递归实现栈的反转
        """
        if stack.empty():
            return  # 🛑 基准情况:栈为空时直接返回
        else:
            num: int = self.bottomOut(stack)  # 🔻 弹出并保存栈底元素
            self.reverse(stack)  # 🔄 递归处理剩余栈
            stack.put(num)  # 🔼 将原栈底元素放入栈顶(实现反转)

    def bottomOut(self, stack: LifoQueue) -> int:
        """
        🔻 移除并返回栈底元素
        🎯 递归地将栈底元素弹出，其他元素保持相对顺序
        📌 返回：被移除的栈底元素
        """
        ans: int = stack.get()  # 🎯 弹出栈顶元素
        if stack.empty():
            return ans  # 🎯 如果栈已空，当前元素就是栈底元素
        else:
            last: int = self.bottomOut(stack)  # 🔄 递归获取真正的栈底元素
            stack.put(ans)  # 🔼 将非栈底元素重新压回栈中
            return last  # 🎯 返回栈底元素


if __name__ == "__main__":
    # 🧪 测试数据: 5 2 0 1 3 1 4 (520 1314)
    test_data = [5, 2, 0, 1, 3, 1, 4]

    # 🔧 创建栈并压入测试数据
    stack = LifoQueue()
    print("📥 原始数据入栈顺序:", test_data)
    for num in test_data:
        stack.put(num)

    # 🔍 查看原始栈的出栈顺序（不反转）
    original_pop = []
    temp_stack = LifoQueue()
    # 先复制栈
    for num in test_data:
        temp_stack.put(num)
    while not temp_stack.empty():
        original_pop.append(temp_stack.get())
    print("📤 原始栈出栈顺序:", original_pop)  # [4, 1, 3, 1, 0, 2, 5]

    # 🔄 执行反转操作
    solution = Solution()
    solution.reverse(stack)

    # 📤 从反转后的栈中取出所有元素
    reversed_result = []
    while not stack.empty():
        reversed_result.append(stack.get())

    print("🔄 反转后出栈顺序:", reversed_result)  # [5, 2, 0, 1, 3, 1, 4]
    print("💖 反转效果: 520 1314 → 1314 520")
    print("✅ 测试完成!")
