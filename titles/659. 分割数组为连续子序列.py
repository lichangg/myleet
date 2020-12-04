#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import defaultdict

#
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dic = defaultdict(list)
        for i in nums:
            if i-1 in dic:
                dic[i - 1].sort(key=lambda x:len(x))
                temp = dic[i-1].pop(0)
                temp.append(i)
                dic[i].append(temp)

                if not len(dic[i-1]):
                    dic.pop(i-1)
            else:
                dic[i].append([i])
        for k,v in dic.items():
            for i in v:
                if 0<len(i)<3:
                    return False
        else:return True
a=Solution().isPossible([1,2,3,3,4,5])
print(a)