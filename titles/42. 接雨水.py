#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 好不容易费尽心思写出来个难的, 本地跑[5, 2, 1, 2, 1, 5]这个能得到正确结果14, 但是网站上总是过不了,说我的程序输出是2
# 二刷时发现上面这句话是错的.因为我方法用成了get_area
# 应该没啥问题
from typing import List


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


# 二刷 思路为从左挡板往后找右挡板 ,从左挡板出发找右挡板貌似太难了..放弃
# class Solution:
#     def get_area(self, nums):
#
#         h = min(nums[0], nums[-1])
#         w = len(nums)
#         sumb = h * w
#         sumb = sumb - 2 * h
#         for i in nums[1:-1]:
#             sumb -= min(i, h)
#         return sumb
#
#     def trap(self, height) -> int:
#         self.area = 0
#         start = 0
#         cur = 1
#
#         while cur < len(height):
#             if height[cur] >= height[start]:
#                 start = cur
#                 cur += 1
#                 continue
#             else:
#                 nums = []
#                 nums.append(height[start])
#                 nums.append(height[cur])
#                 min_h = height[cur]
#                 FLAG=False
#                 cur +=1
#                 while cur < len(height):
#                     min_h = min(min_h, height[cur])
#                     if height[cur] < height[cur - 1] and FLAG:
#                         end = cur -1
#                         cur +=1
#
#                         continue
#
#                         break
#                     else:
#                         if height[cur]>min_h:
#                             FLAG = True
#                         nums.append(height[cur])
#                         cur += 1
#                 self.area += self.get_area(nums)
#                 start = cur-1
#         return self.area
# a=Solution().trap([5,4,1,2])


# 二刷, 用动态规划
class Solution:
    # 这个方法是返回最小容器所盛的雨水量
    def get_area(self, nums):
        if len(nums)<=1 :return 0
        h = min(nums[0], nums[-1])
        w = len(nums)
        sumb = h * w
        sumb = sumb - 2 * h
        for i in nums[1:-1]:
            sumb -= min(i, h)
        return sumb
    def trap(self, height) -> int:
        for index, i in enumerate(height):
            if i!=0:
                # 初始化左挡板
                left = index
                break
        else:
            return 0
        # 生成动态规划数组
        dp=[0 for _ in range(len(height))]
        i = 1
        while i < len(height):
            if height[i]<=height[i-1]:
                dp[i] = dp[i-1]
            else:
                nums = [height[i]]
                # j为寻找当前i位置对应的最大的左挡板位置
                j=i-1
                while 1:
                    nums.append(height[j])
                    if height[j] >= height[i] or j<=left:

                        break
                    j-=1
                if height[i] > height[left]:
                    left = i
                area = self.get_area(nums)

                dp[i] = dp[j] + area
            i+=1
        return dp[-1]


# 一个神奇而且好理解的解法: https://leetcode-cn.com/problems/trapping-rain-water/solution/shuang-zhi-zhen-an-xing-qiu-geng-hao-li-jie-onsuan/
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        SUM,tmp,high=0,0,1
        while(left<=right):
            while(left<=right and height[left]<high):
                SUM+=height[left]
                left+=1
            while(right>=left and height[right]<high):
                SUM+=height[right]
                right-=1
            high+=1
            tmp+=right-left+1
        return tmp-SUM

# 该题还有很多好的解法, 以后看看


a = Solution().trap([5,2,1,2,1,5])
# a = Solution().get_area([3])
print(a)
