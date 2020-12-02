#!/usr/bin/env python
# -*- coding:utf-8 -*-
import bisect
from typing import List
# 学到一个好的排序模块bisect
# bisect有 6 个主要的方法[insort, bisect, insort_left, insort_right, bisect_left, bisect_right]
# 对于一个数a和一个数组nums, insort是不改变原数组的情况下排序并插入a, bisect是看a会处在排序后的nums的哪个索引位置, 至于这两个方法后面带了_left就是
# 在nums中已经有a的情况下需要是往左操作还是右操作
# //TODO
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

# https://leetcode-cn.com/problems/reverse-pairs/solution/python-er-fen-by-powcai/
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = []
        res = 0
        for num in nums:
            # 由于arr是一个有序的列表，所以bisect_right可以返回当前的num*2元素的位置，len(arr) - bisect.bisect_right(arr, num * 2)将得到的是，遍历出来的当前的num所能匹配的翻转对的数量。然后再和res进行累加求得总的翻转对数
            res += len(arr) - bisect.bisect_right(arr, num * 2)
            # bisect.insort(arr, num)
            # 这行代码是将原列表中的元素一个一个的插入空列表，重新生成一个有序的列表
            loc = bisect.bisect_right(arr, num)
            # 用这种切片的方式赋值，而不用下面的方式直接赋值的原因，
            # 是用切片赋值可以避免在对空列表赋值的时候，出现列表赋值索引超出范围的报错的情况。
            # 也就是说，arr[loc:loc] = [num]在对超出索引范围的情况下赋值，或对空列表赋值也是不会报错的。
            arr[loc:loc] = [num]
            # arr[loc]=num
        return res
a=Solution().reversePairs([2,4,3,5,1])
print(a)
