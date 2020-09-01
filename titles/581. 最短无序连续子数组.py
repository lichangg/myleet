#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        temp = []
        i = 0
        j=1
        while j < n:



b=[2, 6, 4, 8, 10, 9, 15]
a=Solution().findUnsortedSubarray(b)
print(a)