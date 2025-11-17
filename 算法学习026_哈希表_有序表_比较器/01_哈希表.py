class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    # 🆔 字符串比较演示
    str1 = "hello"
    str2 = "hello"

    # 🔍 值比较：比较两个字符串的内容是否相同
    print("str1和str2的值是否相同:", str1 == str2)
    # 📍 身份比较：比较两个变量是否指向内存中的同一个对象
    print("str1和str2是否指向内存中的同一个对象:", str1 is str2)
    # 💡 说明：由于Python的字符串驻留机制,相同的字符串字面量会重用同一个对象

    # 🗺️ 内存地址显示
    print(f"str1的内存地址:{id(str1)};str2的内存地址:{id(str2)}")
    # ✅ 验证：由于是同一个对象,所以地址相同
    print(id(str1) == id(str1))  # 由于是同一个对象,所以地址相同
    print()

    # 🎯 用set(集合)来模拟Hashset,默认去重
    set1 = set()
    # ➕ 一次性把str1和str2都添加到set1里面去
    set1.add(str1)
    set1.add(str2)
    # 📊 结果显示：由于字符串内容相同，set会自动去重
    print(set1, len(set1))  # {'hello'}
    print()

    """
    📚 set集合操作方法大全：

    🟢 增加元素：
       ➕ add() - 一次增加一个元素 
       🔄 update(['a','b']) - 一次增加多个元素

    🔴 删除元素：
       ❌ remove('a') - 删除指定元素,元素不存在会报错 
       🎲 pop() - 随机删除并返回一个元素
       ⚠️ discard() - 删除指定元素,元素不存在不会报错 
       🧹 clear() - 清空集合

    🔍 查询操作：
       ✅ in / not in - 判断指定元素是不是在集合中
       📏 len() - 获取集合元素个数
    """

    # 🎯 用dict(字典)来模拟HashMap
    dict1 = {str1: 'world'}
    print(dict1)
    # 🔍 检查键是否存在
    print('str2是不是在dict1里面:', str2 in dict1)
    # 📥 安全获取值
    print('获取str2对应的value:', dict1.get(str2))
    # ⚠️ 获取不存在的键：返回None而不是报错
    print(dict1.get("asss"))  # 获取不存在的键值对:None
    print()

    """
    📚 dict字典操作方法大全：

    🟢 增加元素：
       1. 📝 直接赋值添加 - dict['age']=18 
       2. 🔄 update({'name':'aaa','age':18}) - 批量添加或更新
       3. ⚙️ setdefault("age", 25) - 键不存在时设置默认值,存在时不会修改

    🔴 删除元素：
       1. 🗑️ pop() - 删除指定键并返回值 
       2. 🎲 popitem() - 删除并返回最后一个键值对
       3. ❌ del dict['name'] - 删除指定键值对
       4. 🧹 clear() - 清空字典

    🔄 修改元素：
       1. 📝 直接赋值修改 - dict['age'] = 18 
       2. 🔄 update() - 批量修改

    🔍 查询操作：
       1. 📝 直接通过键访问      
       2. ✅ get() - 安全访问（键不存在返回None）         
       3. 🔎 in 操作符 - 检查键是否存在
       4. 🔑 keys() - 获取所有键   
       5. 💰 values() - 获取所有值    
       6. 📋 items() - 获取所有键值对
       7. 📏 len() - 获取字典大小
    """

    # 🎯 整数键字典演示
    # 创建一个简单的字典
    dict_num: dict[int, int] = dict()
    dict_num[56] = 7285
    dict_num[34] = 3671263
    dict_num[17] = 716311
    dict_num[24] = 1263161
    print(dict_num)

    # 💡 重要技巧:当key的值为整数,范围是固定可控的情况下,可以用数组结构代替哈希表结构
    # 🚀 性能优化:数组访问比哈希表更快，适合笔试竞赛场景
    arr = [-1] * 100
    arr[56] = 7285
    arr[34] = 3671263
    arr[17] = 716311
    arr[24] = 1263161
    # 📝 注意：这里就不打印整个数组了,因为太长了
    print()

    # 🎓 自定义对象作为字典键演示
    # 实例化两个学生对象,把对象作为key值
    s1 = Student("张三", 18)
    s2 = Student("张三", 18)
    # 📝 打印对象：显示对象的默认字符串表示(内存地址信息)
    # print(s1,s2) # 对象的默认字符串表示

    dict_student = dict()
    dict_student[s1] = "这是张三"
    dict_student[s2] = "这是另一个张三"
    # 🔍 观察：虽然两个Student对象内容相同,但Python默认使用对象内存地址作为哈希值
    # 💡 因此s1和s2被视为不同的键,都会存储在字典中
    print(dict_student)
