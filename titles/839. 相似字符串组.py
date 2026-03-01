#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 此处的并查集挂在的字符串, 效率比挂载idx差很多
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UF(strs)
        def issimilar(s1,s2):
            i = 0
            l = len(s1)
            tmp = []
            while i<l:
                if s1[i] != s2[i]:
                    tmp.append(i)
                i+=1
            if len(tmp) != 2:
                return False
            if s1[tmp[0]] != s2[tmp[1]]:
                return False
            return True
        l = len(strs)
        for i in range(l):
            for j in range(i+1, l):
                if issimilar(strs[i], strs[j]):
                    uf.union(strs[i], strs[j])

        return uf.count

class UF:
    def __init__(self,strs):
        self.res = {s:s for s in strs}
        self.count = len(self.res)

    def find(self, x):
        if self.res[x] != x:
            self.res[x] = self.find(self.res[x])
        return self.res[x]
    def union(self, x, y):
        an_x = self.find(x)
        an_y = self.find(y)

        if an_x != an_y:
            #此处注意挂载的是祖先元素, 而不是x,   self[x] = an_y    (这样写是错的)
            self.res[an_x] = an_y
            self.count -= 1

a=Solution().numSimilarGroups(["omv","ovm","arts","star"])
print(a)