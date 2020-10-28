#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        a=Counter(arr)
        s=set()
        for k,v in a.items():
            if v in s:
                return False
            else:
                s.add(v)
        return True

a=Solution().uniqueOccurrences([1,2,2,3,3,3])
print(a)