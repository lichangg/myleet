#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
# 学到了,这个想法太精妙了
#题目要求复杂度是O(n),下面这个方法有for还有while为什么也符合O(n)呢?
#解释: 如果有 x-1那么就不用做了,直接下一位,无论排序如何, 例如 [1,2,3] 只会做1的while 2,3的while都不会做, 再比如[2,1,3] 仍然也只做1的while而不会做2,3的while
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            # 如果这一步没跳出,那就可以保证当前得到的连续序列是以他开始
            if num - 1 in s:
                continue
            curLen = 1
            while num + 1 in s:
                curLen += 1
                num += 1
            res = max(res, curLen)
        return res

# 二刷失败

a=Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print(a)