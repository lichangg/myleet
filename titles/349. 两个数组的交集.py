#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

a=Solution().intersection([1,2],[2,3])
print(a)