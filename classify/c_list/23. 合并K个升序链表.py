#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode, gen_list
# 思路
# 1. 先按头节点排好序(也可以递归中每次都排一次序,这样代码很省事但是倒数第二个测试用例会超时),由于排好了序,所以每次pop(0)必然得到的是当前最小的头节点
# 2. 然后开始递归操作
#     1 弹出当前的最小头部,也就是0号元素, 它的下一个节点指向剩下的lists的结果
#     2 要注意的是,由于当前最小头部被弹出,它原本的下一个节点需要替换它的位置, 但是具体在哪个索引还得一个个比较,最终确定它插入到lists应该在哪儿
#     3 当lists只有一个头节点时退出递归
# 3. 在2.2步的寻找它应该的位置时应该可以用二分查找更快一些, 因为这是有序数组
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        lists = list(filter(None, lists))
        if not lists:
            return
        lists.sort(key=lambda x:x.val)
        def recur(lists):
            if len(lists) == 1:
                return lists[0]
            cur = lists.pop(0)
            tmp= cur.next

            if tmp == None:
                cur.next = recur(lists)
            else:
                for idx,i in enumerate(lists):
                    if tmp.val <= i.val:
                        lists.insert(idx, tmp)
                        break
                else:
                    lists.append(tmp)
                cur.next = recur(lists)

            return cur
        return recur(lists)

# 思路2:分治法, 两两合并

li = []
for i in [[1,4,5],[1,3,4],[2,6]]:
    li.append(gen_list(i))
a=Solution().mergeKLists(li)
print()
