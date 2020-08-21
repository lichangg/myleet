#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import OrderedDict

# 自己写的, 在self.q删除和插入的时候复杂度都为O(n)不符合题意, 若要为O(1)则需要双向链表
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dic = {}
        self.q = list()
    def get(self, key: int) -> int:
        if key in self.dic:
            self.q.remove(key)
            self.q.insert(0, key)
            return self.dic[key]
        else:
            return -1



    def put(self, key: int, value: int) -> None:

        if len(self.dic)>=self.size:
            k = self.q.pop()
            self.dic.pop(k)

        self.dic[key] = value
        self.q.insert(0, key)




# 创建双向链表,双向链表的表头表尾插入操作都是O(1),删除某个节点也是O(1),学到了
# 再用dict维护这个某键存在与否
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # 构建首尾节点, 使之相连
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.lookup = dict()
        self.max_len = capacity

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        if len(self.lookup) == self.max_len:
            # 把表头位置节点删除(说明最近的数据值)
            self.remove(self.head.next)
        self.add(Node(key, value))
    # 删除链表节点
    def remove(self, node):
        del self.lookup[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
    # 加在链表尾
    def add(self, node):
        self.lookup[node.key] = node
        pre_tail = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        pre_tail.next = node
        node.prev = pre_tail


# Python [collections]模块提供的OrderedDict完美适配LRUCache，既有序又能将指定键值对移至末尾。代码如下：
# from collections import OrderedDict
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.d = OrderedDict()
#
#     def get(self, key: int) -> int:
#         v = self.d.get(key, -1)
#         if key in self.d:
#             self.d.move_to_end(key, last=True)
#         return v
#
#     def put(self, key: int, value: int) -> None:
#         self.d[key] = value
#         self.d.move_to_end(key, last=True)
#         if len(self.d) > self.capacity:
#             self.d.popitem(last=False)
#         print(self.d)


cache=LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
