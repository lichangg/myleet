#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 虽然想到了并查集,但是由于没有维护并查集...
# 下面这种方式联通的问题在于假如有四个元素,按遍历顺序来的话0先成一个合集,1跟2联通成一个,要是3能联通0就会先组成[0,3]合集,但同时3也能和[1,2]联通的话就裂开
# class Solution:
#     def numSimilarGroups(self, strs: List[str]) -> int:
#         # 初始化并查集
#         self.dic = {idx: idx for idx in range(len(strs))}
#
#         res = [[0]]
#         i = 1
#         while i < len(strs):
#             for connect in res:
#                 flg = False
#                 for item in connect:
#                     bool_res = self.is_similar(strs[i], strs[item])
#                     if bool_res:
#                         connect.append(i)
#                         flg = True
#                         break
#                 if flg:
#                     break
#
#             else:
#                 res.append([i])
#             i += 1
#         return len(res)
#     def is_similar(self, s1, s2) -> bool:
#         if s1 == s2: return True
#         i = 0
#         diff_index = []
#         while i < len(s1):
#             if s1[i] == s2[i]:
#                 i += 1
#                 continue
#             diff_index.append(i)
#             if len(diff_index) >= 3:
#                 return False
#             i+=1
#         if len(diff_index) == 1:
#             return False
#
#         return s1[diff_index[0]] == s2[diff_index[1]] and s1[diff_index[1]] == s2[diff_index[0]]


# 并查集类型题的标准模板,一定是要维护一个并查集类的
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                bool_res = self.is_similar(strs[i], strs[j])
                if bool_res:
                    uf.union(i, j)
        return uf.count
    def is_similar(self, s1, s2) -> bool:
        if s1 == s2: return True
        i = 0
        diff_index = []
        while i < len(s1):
            if s1[i] == s2[i]:
                i += 1
                continue
            diff_index.append(i)
            if len(diff_index) >= 3:
                return False
            i+=1
        if len(diff_index) == 1:
            return False

        return s1[diff_index[0]] == s2[diff_index[1]] and s1[diff_index[1]] == s2[diff_index[0]]

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
    #寻根并进行路径压缩
    def find(self, x):
        if self.parent[x] == x:
            return x
        #这一步是在进行路径压缩
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[x] = y
            self.count -= 1

a=Solution().numSimilarGroups(["tars","arts","rats","star"])
print(a)