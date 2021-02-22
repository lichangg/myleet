#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


"""
思路:
对于正整数 x，如果区间 [1,x-1]内的所有数字都已经被覆盖，且 x 在数组中，则区间 [1,2x-1] 内的所有数字也都被覆盖。
假设数字 x 缺失，则至少需要在数组中补充一个小于或等于 x 的数，才能覆盖到 x，否则无法覆盖到 x。

如果区间 [1,x-1] 内的所有数字都已经被覆盖，则从贪心的角度考虑，补充 x 之后即可覆盖到 x，且满足补充的数字个数最少。在补充 x 之后，区间 [1,2x-1] 内的所有数字都被覆盖，下一个缺失的数字一定不会小于 2x。

由此可以提出一个贪心的方案。每次找到未被数组覆盖的最小的整数x，在数组中补充 x，然后寻找下一个未被覆盖的最小的整数，重复上述步骤直到区间 [1,n] 中的所有数字都被覆盖。


"""


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, index = len(nums), 0

        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patches += 1

        return patches



# 再刷



a=Solution().minPatches([1,5,100], 20)
print(a)