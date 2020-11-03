#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        cur = float('-inf')
        i = 0
        while i<=len(A)-1:
            if A[i] > cur:
                cur = A[i]
            elif A[i] == cur:
                return False
            else:
                break
            i+=1
        else:
            return False
        if i == 1:
            return False
        while i<=len(A)-1:
            if A[i]<cur:
                cur = A[i]
            else:
                return False
            i+=1
        else:return True
a=Solution().validMountainArray([0,1,2,1,2])
print(a)