import heapq
import bisect
from sortedcontainers import SortedDict, SortedSet
# ⚠️ 注意啊!!! 下载导入这个包,项目名不能够有中文

def floor_key(tree_map, key):
    # 🔍 查找小于等于key的最大键（地板键）
    # 📍 功能：在有序表中找到所有小于等于key的键中最大的那个
    # 将SortedKeysView转换为列表
    keys = list(tree_map.keys())
    # 🎯 使用bisect_right找到第一个大于key的位置，然后减1得到小于等于key的最大位置
    idx = bisect.bisect_right(keys, key) - 1
    if idx >= 0:
        return keys[idx]
    return None  # ❌ 没有小于等于key的元素


# treeMap.ceilingKey(4) 大于等于4且最近的key
def ceiling_key(sorted_map, key):
    # 🔍 查找大于等于key的最小键（天花板键）
    # 📍 功能：在有序表中找到所有大于等于key的键中最小的那个
    # 将键视图转换为列表
    keys = list(sorted_map.keys())
    # 🎯 使用bisect_left找到第一个大于等于key的位置
    idx = bisect.bisect_left(keys, key)
    if idx < len(keys): return keys[idx]
    return None  # ❌ 如果没有找到大于等于key的值


if __name__ == "__main__":
    print("*" * 20, "使用sortedcontainers包中的SortedDict来实现有序表", "*" * 20)
    print()

    """📚 使用sortedcontainers包中的SortedDict来实现有序表"""
    # 🎯 创建有序字典 - 按键的自然顺序自动排序
    tree_map = SortedDict()
    # ➕ 添加键值对（注意：不是按添加顺序，而是按键值排序）
    tree_map[5] = "这是5"
    tree_map[7] = "这是7"
    tree_map[1] = "这是1"
    tree_map[2] = "这是2"
    tree_map[3] = "这是3"
    tree_map[4] = "这是4"
    tree_map[8] = "这是8"
    # 📊 打印有序字典 - 按键的升序排列
    print("打印出这个tree_map(有序的字典)-->", tree_map)
    # 🔍 检查键是否存在
    print("key值为1的在这个表里面是否存在:", 1 in tree_map)
    print("key值为10的在这个表里面是否存在:", 10 in tree_map)
    print()

    # 🔍 查询操作
    print("获取key值为4的键值对的value:", tree_map.get(4))
    # ✏️ 更新操作
    tree_map[4] = "张三是4"
    print("更新后的再查询4:", tree_map.get(4))
    # 🗑️ 删除操作
    tree_map.pop(4)  # 把key为4的那个键值对删除掉
    print("删除掉再查询4:", tree_map.get(4))
    print()

    print("*" * 10, "有序表特有的(哈希表做不到的)", "*" * 10)
    # 🎯 有序表特有操作 - 这些是普通哈希表无法实现的
    # 📍 获取最小的键（第一个元素）
    print("获取所有的key里面最小的key:", tree_map.peekitem(0)[0])
    # 📍 获取最大的键（最后一个元素）
    print("获取所有的key里面最大的key:", tree_map.peekitem(-1)[0])
    # 🔍 地板键：小于等于4的最大键
    print("tree_map中,所有的key小于等于4,且最近的:", floor_key(tree_map, 4))
    # 🔍 天花板键：大于等于4的最小键
    print("tree_map中,所有的key大于等于4,且最近的:", ceiling_key(tree_map, 4))
    print()

    print("-" * 20, "SortedSet来实现有序表,会去重", "-" * 20)
    print()

    """📚 使用sortedcontainers包中的SortedSet来实现TreeSet"""
    # 🎯 创建有序集合 - 自动排序且去重
    tree_set = SortedSet()
    # ➕ 添加元素(重复元素只会保留一个)
    tree_set.add(3)
    tree_set.add(3)
    tree_set.add(4)
    tree_set.add(4)
    print(f"有序表大小 : {len(tree_set)}")
    # 🔄 遍历并弹出所有元素(从小到大)
    while tree_set:
        print(tree_set.pop(0))  # 📍 相当于pollFirst() - 弹出最小的元素
        # 💡 如果要模拟pollLast()，可以使用: print(set.pop())
    print()

    print("*" * 20, "如果不想去重,可以用堆来实现", "*" * 20)
    print()

    # 🎯 使用堆实现有序结构(允许重复元素)
    # 💡 堆:默认小根堆 - 最小的元素总是在堆顶
    heap1 = []
    # ➕ 向堆中添加元素(允许重复)
    heapq.heappush(heap1, 3)
    heapq.heappush(heap1, 3)
    heapq.heappush(heap1, 4)
    heapq.heappush(heap1, 4)
    print(f"堆大小 : {len(heap1)}")
    # 🔄 从小到大弹出所有元素
    while heap1:
        print(heapq.heappop(heap1))  # 📍 弹出并返回最小的元素
