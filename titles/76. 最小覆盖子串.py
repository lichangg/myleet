#!/usr/bin/env python
# -*- coding:utf-8 -*-
#滑动窗口, 收缩指针和扩张指针
#初始化两个指针, 扩张指针向右移动到刚好包含目标字符串后开始收缩,收缩指针收缩到刚好不包括目标字符串后开始扩张
# 这里面有个关键的点是如何判断当前窗口是否已经包含了t字符串:
#    1.
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         dynamic_hashmap = {}
#         for i in t:
#             dynamic_hashmap[i] = dynamic_hashmap.get(i,0) + 1
#         l = 0
#         for index, c in enumerate(s):
#             if c in dynamic_hashmap:
#                 dynamic_hashmap[c] -= 1
#                 l = index

# 学到了
#思路: 用counter动态总计还需要多少字符,用hashmap动态计算每个字符还需要多少个
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        findout = defaultdict(int)
        for i in t:
            findout[i] += 1
        min_len, res = float('inf'), ""
        l, counter = len(s), len(t)
        left = right = 0
        #------------------------------
        while right < l:
            # counter为需要字符总数,所以里面有重复的没有关系,
            # 因为只有当字典中这个字符的值(也就是我还需要多少个这个字符)大于0的时候counter才会减少
            # 所以当counter为0时就可以确定当前窗口已经包含了字符串t
            if findout[s[right]] > 0:
                counter -= 1
            findout[s[right]] -= 1
            right += 1
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                # 此处由于收缩指针是在走扩张指针走过的路.所以无关字符肯定都是小于0的
                # 而相关字符的需求若还是小于0,则说明当前窗口仍然有该相关字符,所以counter不必+1,***只有当相关字符等于0时说明收缩指针再往右走一步则会[刚好不包括]t字符串!!!
                if findout[s[left]] == 0:
                    counter += 1
                findout[s[left]] += 1
                left += 1
        #-------------------------------------
        return res



a=Solution().minWindow("ADOBECODEBANC", "ABC")
print(a)