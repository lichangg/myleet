#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 滑动窗口, 收缩指针和扩张指针, 不过失败了
# 初始化两个指针, 扩张指针向右移动到刚好包含目标字符串后开始收缩,收缩指针收缩到刚好不包括目标字符串后开始扩张
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
# 思路: 用counter动态总计还需要多少字符,用hashmap动态计算每个字符还需要多少个
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        findout = defaultdict(int)
        for i in t:
            findout[i] += 1
        min_len, res = float('inf'), ""
        l, counter = len(s), len(t)
        left = right = 0
        # ------------------------------
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
        # -------------------------------------
        return res


# 二刷超出时间限制, 上面滑动窗口的算法思路很简洁,但是问题在于怎么解决无关字符的问题
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         hashmap = {}
#         count = 0
#         res = []
#         for i in t:
#             hashmap[i] = hashmap.get(i, 0) + 1
#             count += 1
#         i = 0
#         j = 0
#         while i < len(s):
#             if s[i] not in hashmap:
#                 i += 1
#                 continue
#             start = i
#             if j <= i:
#                 j = i
#             if count == 0:
#                 hashmap[s[start]] += 1
#                 res.append(s[start:j])
#                 if hashmap[s[start]] >= 1:
#                     count += 1
#                 i+=1
#                 continue
#             while j < len(s):
#                 if s[j] in hashmap:
#                     if hashmap.get(s[j]) > 0:
#                         count -= 1
#                     hashmap[s[j]] -= 1
#                     if count == 0:
#                         res.append(s[start:j + 1])
#                         hashmap[s[start]] += 1
#                         if hashmap[s[start]] >= 1:
#                             count += 1
#                         j += 1
#                         break
#                 j += 1
#             i += 1
#         min_len = float('inf')
#         min_str = ''
#         for r  in res:
#             if len(r)<min_len:
#                 min_len = len(r)
#                 min_str = r
#         return min_str

# 再刷
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_need = defaultdict(int)
        t_count = 0
        for i in t:
            dic_need[i] += 1
            t_count +=1
        min_len = float('inf')
        min_str = ''

        tmp = []
        i = 0
        l = len(s)
        while i < l:
            if s[i]in dic_need:
                tmp.append(i)
                if dic_need[s[i]] > 0:
                    t_count -=1
                dic_need[s[i]]-=1
                if t_count == 0:
                    start = tmp.pop(0)
                    dic_need[s[start]] += 1
                    if dic_need[s[start]] > 0:
                        t_count += 1
                    while t_count <= 0:
                        start = tmp.pop(0)
                        dic_need[s[start]]+=1
                        if dic_need[s[start]] > 0:
                            t_count +=1
                        else:
                            min_len = min(min_len, i - start + 1)
                    if i-start+1<min_len:
                        min_len = i-start+1
                        min_str = s[start:i+1]
            i+=1
        return min_str
a = Solution().minWindow("bba", "ab")
print(a)
