# 二分查找以及对数器验证
from random import randint  # 🎲 引入随机函数


# ==========================================
# 🐢 [绝对正确的方法] 暴力遍历 O(N)
# ==========================================
def right(arr: list[int], num: int) -> bool:
    n: int = len(arr)
    for i in range(n):
        if arr[i] == num:
            return True
    return False


# ==========================================
# ⚡️ [待测方法] 二分查找 O(logN)
# ==========================================
def exist(arr: list[int], num: int) -> bool:
    n: int = len(arr)
    if n == 0: return False

    l: int = 0
    r: int = n - 1
    m: int = 0

    # 📝 核心循环: 只要区间 [l, r] 有效就继续
    while l <= r:
        # 使用python语言不用担心溢出的问题,
        # 但是要注意: // 表示整除 (向下取整)
        m = (l + r) // 2

        if arr[m] == num:
            return True  # 🎯 找到了
        elif arr[m] > num:
            r = m - 1  # 太大了, 去左边找
        else:
            l = m + 1  # 太小了, 去右边找

    return False


# ==========================================
# 🧪 [对数器] 随机测试逻辑
# ==========================================
def test(n: int, v: int):
    # 1. 生成随机数组: 长度n, 值[1, v]
    arr: list[int] = [randint(1, v) for i in range(n)]

    # 2. ⚠️ 关键: 二分查找必须基于有序数组
    arr.sort()

    # 3. 生成随机目标值
    num: int = randint(0, v)

    # 4. ⚔️ 三重比对:
    # 你的二分 vs 暴力遍历 vs Python内置in
    # 只要有一个结果不一样, 就会报错
    if not (exist(arr, num) == right(arr, num) == (num in arr)):
        print("Something went wrong.")


# ==========================================
# 🚀 主程序
# ==========================================
def main() -> None:
    N: int = 100  # 最大数组长度
    V: int = 1000  # 最大数值范围
    testTime: int = 500000  # 测试次数

    print("Testing Binary Search...")
    for i in range(testTime):
        n: int = randint(0, N)  # 随机本次长度
        test(n, V)

    print("Test is complete. ✅")


if __name__ == '__main__':
    main()
