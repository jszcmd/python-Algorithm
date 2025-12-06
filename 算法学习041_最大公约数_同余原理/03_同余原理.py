"""
题目：同余原理测试与验证

题目要求：
验证两种模运算方法的等价性，计算表达式：
((a + b) * (c - d) + (a * c - b * d)) % mod

具体要求：
1. 实现两种计算方法：
   - f1: 直接计算整个表达式后取模
   - f2: 逐步计算，每一步都及时取模，严格遵循同余原理
2. 验证两种方法的结果是否完全一致
3. 使用模数 mod = 10^9 + 7（常用质数模数）
4. 进行10000次随机测试确保正确性
5. 展示一个具体计算示例

同余原理公式:
1. 加法：(a + b) % m = ((a % m) + (b % m)) % m
2. 减法：(a - b) % m = ((a % m) - (b % m) + m) % m  # +m确保结果非负
3. 乘法：(a * b) % m = ((a % m) * (b % m)) % m

注意：减法操作需要 +mod 确保结果为非负数
"""

import random


# 计算: ((a + b) * (c - d) + (a * c - b * d)) % mod
def f1(a, b, c, d, mod):
    """
    方法一：直接计算法
    直接计算完整表达式后取模
    优点：代码简洁，适合Python等支持大整数的语言
    注意：在其他语言中可能因中间结果溢出而出错
    """
    return ((a + b) * (c - d) + (a * c - b * d)) % mod


def f2(a, b, c, d, mod):
    """
    方法二：逐步取模法
    每一步计算都及时取模，避免中间结果过大
    严格遵循同余原理，适合C++/Java等对整数溢出敏感的语言
    """
    o1 = (a % mod)  # a对mod取模
    o2 = (b % mod)  # b对mod取模
    o3 = (c % mod)  # c对mod取模
    o4 = (d % mod)  # d对mod取模

    o5 = (o1 + o2) % mod  # 计算(a+b) % mod

    # 计算(c-d) % mod，+mod确保结果非负（模运算要求）
    o6 = (o3 - o4 + mod) % mod

    o7 = (o1 * o3) % mod  # 计算(a*c) % mod
    o8 = (o2 * o4) % mod  # 计算(b*d) % mod

    o9 = (o5 * o6) % mod  # 计算((a+b)*(c-d)) % mod

    # 计算(a*c-b*d) % mod，+mod确保结果非负
    o10 = (o7 - o8 + mod) % mod

    ans = (o9 + o10) % mod  # 最终结果取模

    return ans


def main():
    """
    主函数：测试两种方法的等价性
    按照题目要求进行10000次随机测试并展示示例
    """
    print("开始测试:")
    testTimes = 10000  # 测试次数，按题目要求
    mod: int = 10 ** 9 + 7  # 常用模数，素数，常用于算法竞赛和密码学

    # 进行testTimes次随机测试
    for i in range(testTimes):
        # 在[1, mod]范围内生成随机数
        a = random.randint(1, mod)
        b = random.randint(1, mod)
        c = random.randint(1, mod)
        d = random.randint(1, mod)

        # 比较两种方法的结果是否一致
        if f1(a, b, c, d, mod) != f2(a, b, c, d, mod):
            print("出错误了")
            return  # 发现不一致立即终止

    print("测试结束")
    print("所有测试通过，两种方法结果完全一致！")
    print()

    # 显示一个具体示例（题目要求）
    print("随机示例展示:")
    a = random.randint(1, mod)
    b = random.randint(1, mod)
    c = random.randint(1, mod)
    d = random.randint(1, mod)

    print(f"a:{a}")
    print(f"b:{b}")
    print(f"c:{c}")
    print(f"d:{d}")
    print("=======")
    print(f"f1（直接计算）:{f1(a, b, c, d, mod)}")
    print(f"f2（逐步取模）:{f2(a, b, c, d, mod)}")

    # 验证两种方法结果是否相等
    if f1(a, b, c, d, mod) == f2(a, b, c, d, mod):
        print("✅ 结果一致")
    else:
        print("❌ 结果不一致")


if __name__ == '__main__':
    main()
