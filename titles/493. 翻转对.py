#!/usr/bin/env python
# -*- coding:utf-8 -*-
import bisect
from typing import List
# 学到一个好的排序模块bisect
# bisect有 6 个主要的方法[insort, bisect, insort_left, insort_right, bisect_left, bisect_right]
# 对于一个数a和一个数组nums, insort是不改变原数组的情况下排序并插入a, bisect是看a会处在排序后的nums的哪个索引位置, 至于这两个方法后面带了_left就是
# 在nums中已经有a的情况下需要是往左操作还是右操作

# https://leetcode-cn.com/problems/reverse-pairs/solution/zui-jian-dan-yi-shi-xian-de-fang-fa-er-fen-cha-zha/
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tb, res = [], 0
        for n in reversed(nums) :
            res += bisect.bisect_left(tb, n)
            n2 = 2*n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res


a=Solution().reversePairs([2,4,3,5,1])
print(a)
