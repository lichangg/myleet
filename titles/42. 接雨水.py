#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 好不容易费尽心思写出来个难的, 本地跑[5, 2, 1, 2, 1, 5]这个能得到正确结果14, 但是网站上总是过不了,说我的程序输出是2
# 应该没啥问题
class Solution:
    # 计算一个最短盛水容器的所能盛水的面积
    def get_area(self, nums):

        h = min(nums[0], nums[-1])
        w = len(nums)
        sumb = h * w
        sumb = sumb - 2 * h
        for i in nums[1:-1]:
            sumb -= min(i, h)
        return sumb

    def trap(self, height) -> int:
        all = 0
        end = 0
        for index, i in enumerate(height[0:-1]):
            if index < end or i <= height[index + 1]:
                continue
            # if i !=0:
            start = index
            cur = index
            down = index
            end = 0
            while cur < len(height) - 1:
                cur += 1
                if height[cur] < height[down]:
                    down = cur
                    continue
                if (cur != len(height) - 1 and height[cur] >= height[cur + 1]) or (
                        cur == len(height) - 1 and height[cur] != 0):
                    end = cur
                    break
            if end:
                all += self.get_area(height[start:end + 1])
        return all

# 二刷 思路为从左挡板往后找右挡板
class Solution:
    def trap(self, height) -> int:

# a=Solution().trap([5,4,1,2])
a = Solution().get_area([5, 2, 1, 2, 1, 5])
