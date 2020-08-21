#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
#遍历得到每个点所能达到的最大位置
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

a=Solution().canJump([2,3,1,0,0,4])
print(a)