#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
#遍历得到每个点所能达到的最大位置
from typing import List


class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  #更新最远能到达位置
            if max_i >= len(nums):
                return True
            #如果当前索引已经大于了最大位置可以提前返回False
            if i>max_i:
                return False
        return max_i>=i

# 二刷动态规划失败，上面方法极度简单，多看看



# 再刷
# 设dp[i]为当前位置最远能到达的位置
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [0] * l
        i = 0
        while i<l:
            if i <= dp[i-1]:
                dp[i] = max(nums[i]+i, dp[i-1])
            else:
                return False
            i+=1
        return True


a=Solution().canJump([2,3,1,1,0,4])
print(a)