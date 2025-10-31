""" 二叉树的层序序列化与反序列化 """


# 测试链接:https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
# 注意提交的时候不要提交下面的TreeNode这个类


# 二叉树节点的定义
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 准备好一个足够长度的队列
    node_queue = [None] * 10001

    # 层序序列化,返回一个字符串
    def serialize(self, root):
        """
        将一棵二叉树编码为一个字符串
        参数root:要进行序列化的树的根节点
        要返回的类型:字符串
        """
        node_arr = []  # 初始化一个node_arr数组,用来存放所有的节点

        if root:  # 如果根节点不为空
            # 节点不为空,进队列,序列化
            # 节点为空,不进队列但是要序列化
            node_arr.append(str(root.val))  # 先把根节点root序列化
            l = 0
            r = 0  # 初始化队列,这里用局部变量l,r就够用
            self.node_queue[r] = root  # 把根节点加入到队列
            r += 1  # 更新队尾指针
            while l < r:  # 队列里面有东西
                cur = self.node_queue[l]  # 弹出队列顶部的元素
                l += 1  # 更新队头指针
                if cur.left:  # 有左节点,既加入到队列,又序列化
                    node_arr.append(str(cur.left.val))  # 左节点序列化
                    self.node_queue[r] = cur.left  # 左节点加入到队列
                    r += 1  # 更新队尾
                else:
                    node_arr.append("#")  # 没有左节点,只序列化,不用加入队列
                if cur.right:  # 有右节点,既加入到队列,又序列化
                    node_arr.append(str(cur.right.val))  # 右节点序列化
                    self.node_queue[r] = cur.right  # 把右节点加入队列
                    r += 1  # 更新队尾
                else:
                    node_arr.append("#")  # 没有右节点,不加入队列但是序列化

        return ",".join(node_arr)  # 返回字符串

    # 层序反序列化,返回头节点
    def deserialize(self, data):
        """将data编码数据解码为二叉树
        参数data:二叉树的字符串数据
        返回值:解码成功的root头节点
        """
        if data == "": return None  # 得到空字符串,root就是空树
        node_arr = data.split(",")  # 分割字符串得到node_arr数组
        index = 0
        root = self.create(node_arr[index])  # 先把根节点root创建出来
        index += 1

        l = 0
        r = 0  # 初始化队列
        self.node_queue[r] = root  # 把根节点入队列
        r += 1  # 更新队尾r
        while l < r:  # 队列里面有东西
            cur = self.node_queue[l]  # 取出队列头部的节点
            l += 1  # 更新队尾r
            # cur的左右孩子直接消费,
            cur.left = self.create(node_arr[index])  # 建出左孩子
            index += 1
            cur.right = self.create(node_arr[index])  # 建立右孩子
            index += 1
            # 建出来的节点如果不为空,就加入到队列,先加左在加右
            if cur.left:  # 左节点不为空
                self.node_queue[r] = cur.left  # 左节点入队列
                r += 1
            if cur.right:  # 右节点不为空
                self.node_queue[r] = cur.right  # 右节点入队列
                r += 1
        return root

    # 创建节点的函数
    def create(self, value):
        if value == "#": return None  # 当前字符是"#",就返回一个空节点
        return TreeNode(int(value))  # 当前字符不是"#",返回正常建出来的节点

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
