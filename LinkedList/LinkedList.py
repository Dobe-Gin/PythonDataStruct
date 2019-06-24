# 单向链表
# data：root、length
# method：__init__ append appendleft remove find popleft headnode clear


#定义一个node节点
class Node:
    def __init__(self,value=None,next=None):
        self.value,self.next = value,next


#定义链表
class LinkedList:
    def __init__(self,maxsize = None):
        self.maxsize = maxsize
        # 定义根节点
        self.root = Node()
        # 定义链表长度
        self.length = 0
        # 定义未节点
        self.tailnode = None

    def __len__(self):
        return self.length

    def append(self,value):
        # 先判断链表长度
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("NodeLis is full")
        node = Node(value)
        # 获取未节点
        tailnode = self.tailnode
        # 判断未节点是不是空，空就就是讲明是从根节点出发，根节点为链表入口
        if tailnode is None:
            self.root.next = node
        else:
            # 如果未节点不是空，未节点指向当前添加的值
            tailnode.next = node
        # 更新未节点
        self.tailnode = node
        # 更新长度
        self.length += 1

    # 往左边添加节点
    def appendleft(self,value):
        # 先判断链表长度
        if self.maxsize is not Node and len(self) > self.maxsize:
            raise Exception("NodeLis is full")
        # 获取头节点
        headnode = self.root.next
        node = Node(value)
        # 更新头节点
        self.root.next = node
        node.next = headnode
        # 更新长度
        self.length += 1

    # 遍历链表
    def iter_nodelist(self):
        # 获取根节点
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            # 更新当前节点
            curnode = curnode.next
        # 取出未节点
        yield curnode

    # 遍历操作
    def __iter__(self):
        for node in self.iter_nodelist():
            yield node.value
    # 打印
    def __str__(self):
        return "NodeList{node},length={length}".format(node=[node.value for node in self.iter_nodelist()],length=self.length)

    def __repr__(self):
        return self.__str__()

    # 删除node ，O(n)
    def remove(self,value):
        prevnode = self.root
        for curnode in self.iter_nodelist():
            if curnode.value == value:
                #被删除的节点的上一个节点指向被删除的节点的下一个节点
                prevnode.next = curnode.next
                if curnode is self.tailnode:
                    # 更新prevnode
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                # 表示删除成功
                return "remove {} ok".format(value)
            else:
                # 更新prevnode
                prevnode = curnode
        # 表示删除失败
        return "remove {} fail".format(value)

    # 查找node，O(n)
    def find(self,value):
        index = 0
        for node in self.iter_nodelist():
            if node.value == value:
                return index
            index += 1
        return false

    # 删除左边第一个节点，pop，O(1)
    # 把头节点删除，让root节点指向头节点的下一个节点
    def popleft(self):
        if self.root.next is None:
            raise Exception("pop from empty LinkedList")
        headnode = self.root.next
        self.root.next = headnode.next()
        value = headnode.value
        del headnode
        return value

    # 清除链表
    def clear(self):
        # 遍历删除节点
        for node in self.iter_nodelist():
            del node
        self.root.next = None
        self.length = 0



if __name__ == '__main__':
    # 测试
    def test_linked_list():
        l = NodeList()
        l.append(1)
        l.append(3)
        l.append(5)

        assert len(l) == 3
        assert l.find(3) == 1

        l.remove(1)
        assert len(l) == 2
        print(len(l))
        print(l.remove(4))
        print(l.remove(5))
        print(l)
        print(l.remove(5))

    test_linked_list()
