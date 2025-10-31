""" 二叉树的正序序列化与反序列化 """


# 测试链接:https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
# 注意提交的时候不要提交下面的TreeNode这个类

# 二叉树节点的定义
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    count = 0  # 当前数组消费到哪了

    # 把根节点为root的树,序列化成字符串
    def serialize(self, root):
        """
        将一棵二叉树编码为一个字符串
        参数root:要进行序列化的树的根节点
        要返回的类型:字符串 比如: 1,2,#,#,3,4,#,#,5,#,#
        """
        node_arr = []  # 创建一个节点数组(字符数组),把所有的节点都按先序放进去
        self._encode(root, node_arr)  # 把这个树序列化加入到数组node_arr里面
        return ",".join(node_arr)  # 以逗号拼接整个字符数组,转成字符串

    # _edcode函数,把node以及node的子树的节点收集到数组里面的;类似递归先序遍历二叉树
    # 同时告诉别人这是一个私有函数,不要直接调用
    def _encode(self, node, node_arr):
        # 如果当前node为空,我们就把字符"#"添加到数组里面
        if not node:
            node_arr.append("#")
        else:  # node节点不为空的情况下:先把node节点加进去,再去子树
            node_arr.append(str(node.val))  # 把当前node节点的val值先转成字符串再加入到数组
            self._encode(node.left, node_arr)  # 把左树序列化加入到数组里面
            self._encode(node.right, node_arr)  # 把右树序列化加入到数组里面

    # 把data字符串数据解码成二叉树
    def deserialize(self, data):
        """将data编码数据解码为二叉树
        参数data:二叉树的字符串数据
        返回值:解码成功的root头节点
        """
        self.count = 0  # 每一次使用这个反序列化的函数都要初始化count=0
        node_arr = data.split(",")  # 先把字符串转成数组
        return self._decode(node_arr)  # 返回根节点

    # 递归创建node_arr数组里面的节点
    def _decode(self, node_arr):
        cur = node_arr[self.count]  # 把第count位置的字符取出
        self.count += 1  # count++
        if cur == "#":
            return None  # 如果当前字符是"#",原来这个位置是None
        else:  # 注意这和else要注意加上
            node = TreeNode(int(cur))  # cur是数字字符,转成整数,创建这个节点
            node.left = self._decode(node_arr)  # 继续消费count,去建立左树
            node.right = self._decode(node_arr)  # 继续去消费,去建立右树
            return node  # 返回建立的头节点

# 您的Codec对象将被实例化并以此方式调用:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
