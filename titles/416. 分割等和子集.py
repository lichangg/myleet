#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 这个问题可以做如下简化
# 首先算出总和sum
# 再计算前k(0 < k < len(nums))个数能否合成 sum/2
# 而上述问题可以转为0-1背包问题,神奇
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """dp"""
        if not nums or len(nums) == 1:  return False  # nums为空或者nums中只有一个元素
        if sum(nums)%2:  return False  # sum(nums)是奇数
        sum_nums = sum(nums)
        target = sum_nums // 2
        # 定义dp，dp[i][j]表示nums[0:i+1]中是否存在一些元素的和等于j+1
        # 行的取值从0到len(nums)-1, 用i表示，每一行代表一个物品
        # 列的取值从0到target-1，用j表示，每一列代表一个容量为j+1的背包
        # 最终结果返回dp[len(nums-1)][target-1]
        dp = [[False]*target for _ in range(len(nums))]

        # 一般来说dp需要初始化第一行和第一列
        dp[0][nums[0]-1] = True  # 初始化第一行，将nums[0]放到容量为nums[0]的背包

        for i in range(1, len(nums)):  # 从第二个物品开始遍历(因为第一个物品已经放了)
            for j in range(target):  # 遍历每个背包
                # 注意第j个背包的容量是j+1

                # ij状态可以转移到dp[i-1][j] (意思就是不要当前的数nums[i])
                # 或者可以转移到dp[i-1][j-nums[i]] (意思就是要当前的数nums[i],但是必须是刚好给我留够了
                # nums[i]的空间, 而dp[i-1][j-nums[i]]为True就代表确实刚好留够了)
                if nums[i] < j+1:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                # 当前数nums[i]刚刚能装满容量j+1
                elif nums[i] == j+1:
                    dp[i][j] = True
                # 当前数比容量还大, 那就肯定要不了当前数, 直接转移到dp[i-1][j]就行了
                elif nums[i] > j+1:
                    dp[i][j] = dp[i-1][j]

        return dp[len(nums)-1][target-1]

a=Solution().canPartition([1, 5, 11, 5])
print(a)