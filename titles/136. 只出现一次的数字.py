#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import reduce
from typing import List


# 1. 异或操作使得相同的数异或之后始终为0,学到了
# 2. 0和任何相同的数异或等于该数本身
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

# 这种方法也挺骚的,只不过set操作会用额外空间
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)
