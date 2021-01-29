#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路
# 1. 维护一个单调递减的栈(栈内存索引而不是数值)和一个右边界索引, 因为左边界索引可以通过k算出来, 所以不用维护左边界索引
# 2. 利用前k个数字初始化该栈, 在之后的滑动中, 栈顶元素始终时窗口内最大的元素
# 3. 开始滑动窗口
#   - 每次判断栈顶元素是不是已经小于左边界了, 若小于则必须弹出
#   - 每次从右边界加进来的元素若大于栈尾元素则对栈发起弹出操作, 结束之后加入栈尾
# 4. 每经历一次完滑动后, 结果列表里面加入栈顶元素, 然后重复第三步
class Solution:
    def maxSlidingWindow(self, nums, k):
        max_list = []
        l = len(nums)
        if l <= k:
            return [max(nums)]
        right = k - 1
        # 初始化栈
        stack = []
        for i in range(k):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)

        # 窗口开始滑动
        while right < l:
            # 先进行判断, 将栈顶元素始终维持在大于等于左边界的位置
            while stack and stack[0] < right - k + 1:
                stack.pop(0)

            while stack and nums[stack[-1]]<= nums[right]:
                stack.pop()
            stack.append(right)
            max_list.append(nums[stack[0]])
            right +=1
        return max_list
a=Solution().maxSlidingWindow([1,3,1,2,0,5], k = 3)
print(a)