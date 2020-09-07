#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 结论1. 最小堆里面的元素与元素之间必须要可以进行大小对比,例如int和int比, list和list比等等, int和list比就不行
# 结论2. list和list对比的时候默认只比较第一个元素的大小
import heapq

from utils.util_funcs import ListNode

hq= []
test1=[5,9,1,54,3,98,72,96,498,598,4,98]
test2=[[18,3],[5,2],[7,6],[1,19],0]
# for i in test2:
#     heapq.heappush(hq, i)
a=[4,1]
b=[3,2]
print(a<b)
if None:
    print(1)