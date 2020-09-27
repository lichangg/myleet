#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 多种方法
# 方法1: 暴力法,时间复杂度为O(nk)
# 方法2: 维护一个最大堆, 最大堆插入一个元素消耗的时间为log(k),所以时间复杂度是O(nlog(k))
# 方法3: 维护一个双端队列, 该队列里面记录元素的索引, 时间复杂度是O(n)

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # 这种情况表明窗口的起始位置已经超过了最大值的索引,所以需要把该索引去除
            if deq and deq[0] == i - k:
                deq.popleft()
            # 因为当前的索引i是最新的, 所以它对应的值要是比队列内某个索引对应的值A大的话那A就再也不可能作为后续窗口中最大的了,所以去除
            # 该处即便用了while,但是复杂度仍为O(n)的原因是:
            #   1.如果当前i比队列最后一个要小的话不会进入循环
            #   2.如果当前i比队列最后一个要大的话就会循环删除,未来当下一个i进来时若比当前i要大只需要循环删除1次, 当下一个i进来比当前i小时仍然不会进入循环
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # 初始化双端队列和输出数组的第0个值
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

# 二刷时有点看懂了, 非常精髓
# 方法4: 动态规划,暂时没看懂
# 思路: 滑动窗口长度为k, 可以先假想滑动窗口每次滑动的距离也为k(此为方式1), 此时求输出滑动窗口最大值列表就很简单, 每隔k隔元素遍历窗口求最大值就行,此时最大值的个数为n/k (若余数不为0则向上取整)
# 目前窗口之间的信息是不互通的
# 但是题目的滑动窗口不是每次移动k而只移动1步(此为方式2),这就要求在滑动的时候处在各窗口之间的数的信息需要连接起来
# 要达到这个效果可以生成两个统计数组left和right,
# left统计方式1中每个窗口从左向右的最大值
# right统计方式1中每个窗口从右向左的最大值
# 这样两个数组可以获得最全的最大值信息
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


# 二刷, 先暴力, 很明显会超时
import heapq


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if len(nums) <= k:
            return [max(nums)]
        i = k
        res = []
        while i <= len(nums):
            # 注意
            res.append(max(nums[i - k:i]))
            # 注意, 下行代码的效率没比上面的高
            # res.append(heapq.nlargest(1, nums[i - k:i])[0])
            i += 1
        return res

# 二刷, 看题解后尝试用双端队列维护最大值窗口
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(index):
            if self.deq and index - self.deq[0] >= k:
                self.deq.popleft()

            while self.deq and nums[self.deq[-1]] <= nums[index]:
                self.deq.pop()

        self.deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            self.deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        res = [nums[max_idx]]


        for i in range(k, len(nums)):
            clean_deque(i)
            self.deq.append(i)
            res.append(nums[self.deq[0]])
        return res

a = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(a)
