""" 二叉树的锯齿形层序遍历:填函数风格 """
# 测试链接:https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional, List


# 二叉树节点类的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" 方法(1):普通层序遍历的结果的部分逆序处理 """


# 注意提交的时候把类名改成Solution直接复制到力扣里面;

class Solution1:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                cur = all_nodes[head]  # 取出此时队列头部的元素
                head += 1  # head+1,head指向下一个位置
                level_nodes.append(cur.val)  # 把cur.val加入到这一层的数组里面

                if cur.left:  # 有左节点,加入到队列
                    all_nodes[tail] = cur.left
                    tail += 1
                if cur.right:  # 有右节点,加入到队列
                    all_nodes[tail] = cur.right
                    tail += 1
            # 把每一层的遍历收集到的值,连带整个数组,都追加到ans里面
            ans.append(level_nodes)

        # 第一层:正序,第二层:逆序;第三层:正序...  --- 使用列表推导式实现
        return [ans[i] if i % 2 == 0 else ans[i][::-1] for i in range(len(ans))]


""" 方法(2):在遍历的时候,添加到数组里面的时候处理顺序 """


# 注意提交的时候把类名改成Solution直接复制到力扣里面;

class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

        reverse = False  # 增加一个变量reverse,初始为False
        # reverse 为False,下面正常遍历;
        while head < tail:  # 如果head<tail,说明队列里面还有东西
            size = tail - head  # (1):拿队列长度size
            level_nodes = []

            # 第一步:队列中这size个原来有的节点的值加入到level_nodes里面
            # reverse == False,从左往右遍历, l......r-1,收集size个
            # reverse == True, 从右往左遍历, r-1......l,收集size个
            if reverse:  # reverse == False
                for i in range(tail - 1, head - 1, -1):
                    cur = all_nodes[i]
                    level_nodes.append(cur.val)
            else:  # reverse == True
                for i in range(head, tail):
                    cur = all_nodes[i]
                    level_nodes.append(cur.val)

            # 第二步:这个for循环现在就是处理这些原来的size个节点
            # 把这原来的size个节点都一个一个从队头弹出,弹出后加入子节点,为下一层做准备
            for i in range(size):  # 控制下面步骤(2):执行size次
                cur = all_nodes[head]  # 取出此时队列头部的元素
                head += 1  # head+1,head指向下一个位置

                if cur.left:  # 有左节点,加入到队列
                    all_nodes[tail] = cur.left
                    tail += 1
                if cur.right:  # 有右节点,加入到队列
                    all_nodes[tail] = cur.right
                    tail += 1
            # 把每一层的遍历收集到的值,连带整个数组,都追加到ans里面
            ans.append(level_nodes)
            # 这一层遍历完后,把reverse取反,下一层的顺序和这一层的相反
            reverse = not reverse

        return ans
