#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 常规解法,但是不合题意
# 时间空间复杂度都为O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res=[]
        for i in range(1,len(nums) +1 ):
            if i not in s:
                res.append(i)
        return res
# 方法二：原地修改
# 我们需要知道数组中存在的数字，由于数组的元素取值范围是 [1, N]，所以我们可以不使用额外的空间去解决它。
# 我们可以在输入数组本身以某种方式标记已访问过的数字，然后再找到缺失的数字。
# 算法：
#
    # 遍历输入数组的每个元素一次。
    # 我们将把 |nums[i]|-1 索引位置的元素标记为负数。即 nums[|nums[i] |- 1] \times -1nums[∣nums[i]∣−1]×−1 。
    # 然后遍历数组，若当前数组元素 nums[i] 为负数，说明我们在数组中存在数字 i+1。
# 最后仍为正数的元素的[索引+1]就是缺失的数字,我吐了,学到了
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):

            new_index = abs(nums[i]) - 1


            if nums[new_index] > 0:
                nums[new_index] *= -1

        # Response array that would contain the missing numbers
        result = []

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result


b=[4,3,2,7,8,2,3,1]
a=Solution().findDisappearedNumbers(b)
print(a)
