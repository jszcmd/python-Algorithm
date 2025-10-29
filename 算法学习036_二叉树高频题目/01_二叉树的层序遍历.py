""" 二叉树的层序遍历 """
# 测试链接:https://leetcode.cn/problems/binary-tree-level-order-traversal/
from typing import Optional, List


# 二叉树节点类的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" (1):普通bfs来处理 """
# 注意提交时的时候把下面的导包也赋值上,类名改成Solution直接复制到力扣里面
from collections import deque  # 使用内置的双端队列


class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []  # root节点为空,直接返回一个空数组[]

        ans = []  # 初始化一个数组,后面要返回出去
        all_nodes = deque()  # 初始化一个队列
        levels = {}  # 用集合实现的哈希表,key=节点对象:value=节点的层数(从1,2)
        all_nodes.append(root)  # 把根节点加入到队列中
        levels[root] = 0  # 向字典里面加入{root:0}

        while all_nodes:  # 如果队列不为空就一直执行
            cur = all_nodes.popleft()  # 弹出队列头部的元素
            level = levels[cur]  # 记录当前节点的层数
            # 如果ans的大小等于当前层级,说明需要新建一个子列表
            if len(ans) == level: ans.append([])
            ans[level].append(cur.val)  # 向ans中的ans[level]数组中添加一个元素cur.val
            if cur.left:  # 有左节点,把左节点压入到队列里面
                all_nodes.append(cur.left)
                levels[cur.left] = level + 1  # 同时把再把key=节点对象,value=level+1(父节点的下一层)加入到字典里面
            if cur.right:  # 有右节点,把右节点加入到队列里面
                all_nodes.append(cur.right)
                levels[cur.right] = level + 1  # 同时把再把key=节点对象,value=level+1(父节点的下一层)加入到字典里面

        return ans


""" (2):每次处理一层的优化bfs """


# 提交的时候注意把类名改成Solution

class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []  # 如果root节点是空的，直接返回空列表

        all_nodes = [None] * 2001  # 准备一个长度为2001的数组(节点最多为2000个)
        # 用这个all_nodes来实现队列,我们只需要对数据加入和删除一次就足够
        ans = []  # 准备一个空的数组,用来存放每一层的节点(也是我们要返回的)
        # 我们需要返回arr=[[],[],[]]数组嵌套数组的形式
        head = 0  # head表示队列头部元素的索引值,删除队列头部元素直接把head+1就可以
        tail = 0  # tail表示队列尾部的下一个位置的索引值,添加元素直接添加到tail位置,然后tail+1

        # 当head == tail的时候,说明当前队列里面没有元素
        # 当head < tail的时候,说明当前队列里面还有元素
        # 由于是用一个普通数组实现的队列,不会出现head > tail的情况(循环队列可能出现head>tail)

        # 首先把root根节点加入到节点数组里面去
        all_nodes[tail] = root
        tail += 1

        while head < tail:  # 如果head<tail,说明队列里面还有东西
            size = tail - head  # (1):拿队列长度size
            level_nodes = []

            # (2):弹出队列头部的节点,这个节点有左节点,加入队列;有右节点,加入队列
            # 步骤(2)执行size遍(这个size就是上面拿到的那个size,即使后面变了,还是用上面那一个)
            # 这个for循环会把整个一层的节点的值放入到level_nodes里面去
            for i in range(size):  # 控制下面步骤(2):执行size次
                # (a):处理原来的size个节点,获取值,加入到列表后,从队列弹出
                cur = all_nodes[head]  # 取出此时队列头部的元素
                head += 1  # head+1,head指向下一个位置
                level_nodes.append(cur.val)  # 把cur.val加入到这一层的数组里面

                # (b):把子节点添加到队列里面,为下一层遍历做准备
                if cur.left:  # 有左节点,加入到队列
                    all_nodes[tail] = cur.left
                    tail += 1
                if cur.right:  # 有右节点,加入到队列
                    all_nodes[tail] = cur.right
                    tail += 1
            # 把每一层的遍历收集到的值,连带整个数组,都追加到ans里面
            ans.append(level_nodes)

        return ans
