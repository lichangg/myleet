#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode

# 思路1. 不断的二分
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 2:
            # 这里注意root和左节点的位置
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        l = len(nums)
        mid = l//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
Solution().sortedArrayToBST([-10,-3])