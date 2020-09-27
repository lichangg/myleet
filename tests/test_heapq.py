#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 结论1. 最小堆里面的元素与元素之间必须要可以进行大小对比,例如int和int比, list和list比等等, int和list比就不行
# 结论2. list和list对比的时候默认只比较第一个元素的大小
import heapq

from utils.util_funcs import ListNode

hq= []
test1=[5,9,1,54,3,98,72,96,498,598,4,98]
for i in test1:
    heapq.heappush(hq, i)
print(hq[0])