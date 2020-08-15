#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def groupAnagrams(self, strs):
        hashmap = {}
        for i in strs:
            li_i = list(i)
            li_i.sort()
            key = ''.join(li_i)
            if hashmap.get(key, ''):
                hashmap[key].append(i)
            else:
                hashmap[key] = [i]
        res = []
        for k,v in hashmap.items():
            res.append(v)
        return res
# 别人的方法， 简洁一点
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dict = {}
#         for item in strs:
#             key = tuple(sorted(item))
#             dict[key] = dict.get(key, []) + [item]
#         return list(dict.values())

a=Solution().groupAnagrams([])
print(a)




