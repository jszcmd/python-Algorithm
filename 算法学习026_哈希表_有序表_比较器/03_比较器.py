from functools import cmp_to_key

from sortedcontainers import SortedSet


class Employee:
    def __init__(self, company, age):
        self.company = company
        self.age = age

    # 🆔 为了在TreeSet类似功能中区分不同对象,重写__repr__
    # 📍 作用:在打印对象时显示有意义的信息,而不是默认的内存地址
    def __repr__(self):
        return f"Employee(company={self.company}, age={self.age})"

    # 也可以在类中直接定义两个Employee对象的比较方法
    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age


# 🎯 自定义比较器类,类似Java的Comparator
class EmployeeComparator:
    @staticmethod
    def compare(o1: Employee, o2: Employee):
        # 📚 比较器规则说明:
        # 🔻 返回负数表示o1优先级更高(排在前面)
        # 🔺 返回正数表示o2优先级更高(排在后面)
        # ➖ 返回0表示两者相等
        return o1.age - o2.age
        # 💡 等价于以下逻辑：
        # """谁的年龄小:谁的优先级更高"""
        # if o1.age < o2.age: return -1
        # elif o1.age > o2.age: return 1
        # else: return 0


# 🎯 多级比较器:公司小的在前面,如果公司相同,谁年龄小,谁在前面
def company_then_age(a: Employee, b: Employee):
    # 1️⃣ 第一优先级：按公司编号升序
    if a.company != b.company: return a.company - b.company
    # 2️⃣ 第二优先级：公司相同则按年龄升序
    return a.age - b.age


if __name__ == "__main__":
    # 👥 创建员工对象数组
    s1 = Employee(2, 27)
    s2 = Employee(1, 60)
    s3 = Employee(4, 19)
    s4 = Employee(3, 23)
    s5 = Employee(1, 35)
    s6 = Employee(3, 55)
    arr = [s1, s2, s3, s4, s5, s6]

    print("*" * 10, "使用自定义比较器排序(年龄小的在前面)", "*" * 10)
    # 🔄 使用自定义比较器排序 - 按年龄升序
    arr_sorted = sorted(arr, key=cmp_to_key(EmployeeComparator.compare))
    # 📊 打印排序结果
    print(*[f"{e.company} , {e.age}" for e in arr_sorted], sep='\n')
    print()

    print("*" * 10, "使用lambda表达式按年龄降序排序(年龄大的在前面)", "*" * 10)
    # 🔄 使用lambda表达式实现降序排序
    arr_sorted = sorted(arr, key=cmp_to_key(lambda a, b: b.age - a.age))
    print(*[f"{e.company} , {e.age}" for e in arr_sorted], sep='\n')
    print()

    print("*" * 10, "先按公司编号升序,公司相同则按年龄升序(公司小在前,公司相同年龄小在前)", "*" * 10)
    # 🔄 多级排序：先公司后年龄
    arr_sorted = sorted(arr, key=cmp_to_key(company_then_age))
    print(*[f"{e.company} , {e.age}" for e in arr_sorted], sep='\n')
    print()

    # 📚 使用SortedSet生成有序表说明:
    # ✅ 如果是str,int等内置类型,SortedSet会自动知道如何比较
    # 🎯 对于自定义数据类型,必须提供比较策略
    print("*" * 10, "使用SortedSet生成有序表排序(公司小在前,公司相同年龄小在前),python默认是不去重", "*" * 10)
    # 🏗️ 创建有序集合,传入自定义比较器
    sorted_set = SortedSet(arr, key=cmp_to_key(company_then_age))

    print("初始sortedset大小:", len(sorted_set))
    """📝 注意：这里添加重复的元素不会去重,因为Employee对象是不同的实例"""
    # ➕ 添加重复元素(内容相同但对象不同)
    sorted_set.add(Employee(2, 27))
    print("添加重复元素后的大小:", len(sorted_set))
    # ➕ 添加新元素
    sorted_set.add(Employee(4, 29))
    print("添加新元素后的大小:", len(sorted_set))
    # 📊 打印排序好的有序集合
    print(*[f"{e.company} , {e.age}" for e in sorted_set], sep='\n')
