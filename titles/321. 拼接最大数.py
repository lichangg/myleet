#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 此题可连接 402

from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 用单调栈的方法取长度为k的最大子序列
        def func(nums, k):
            stack_1 = []
            for i in range(len(nums)):
                while stack_1 and len(nums) - i > k - len(stack_1) and nums[i] > stack_1[-1]:
                    stack_1.pop()
                if len(stack_1) < k:
                    stack_1.append(nums[i])
                else:
                    continue
            return stack_1

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        max_ans = []
        # k得+1,注意点儿
        for i in range(k + 1):
            f1 = func(nums1, i)
            f2 = func(nums2, k - i)
            f_merge = merge(f1, f2)
            if len(f_merge) > len(max_ans):
                max_ans = f_merge
            elif len(f_merge) < len(max_ans):
                pass
            else:
                max_ans = max(f_merge, max_ans)
        return max_ans


# 上面我写的2088ms,这个只要280ms,最后一行能过吗???看不懂
class Solution:
    def maxNumber(self, nums1, nums2, k):
        # 也是找最大的子序列,只不过我的方法是留下元素, 他的方法是剔除元素
        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger.pop(0))
            return ans

        return max(merge(pick_max(nums1, i), pick_max(nums2, k - i)) for i in range(k + 1) if
                   i <= len(nums1) and k - i <= len(nums2))


# a=Solution().maxNumber(nums1 = [3, 4, 6, 5],nums2 = [9, 1, 2, 5, 8, 3],5)
a = Solution().maxNumber(nums1=[6, 7], nums2=[], k=2)
print(a)
