#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import OrderedDict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        for i in s:
            if i in dic_s:
                dic_s[i] +=1
            else:
                dic_s[i] = 1
        dic_t = {}
        for j in t:
            if j in dic_t:
                dic_t[j] +=1
            else:
                dic_t[j] = 1
        return dic_s == dic_t

a=dict({'a':1, 'b':2})
b=dict({'b':2, 'a':1})
print(a == b)
