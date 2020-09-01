#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 暴力法,复杂度为O(2**N)
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         cnt, n =  0, len(nums)
#         for i in range(n):
#             for j in range(i, n):
#                 if (sum(nums[i:j + 1]) == k):
#                     cnt += 1
#         return cnt

# 暴力解法(优化版)复杂度为O(N**2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            prefixsum = 0
            for j in range(i, len(nums)):
                # 此处就是在计算[i,j]的总和,判断是否和k相等,而[i,j]的总和实际上是[0,j]的总和减去[0,i]的总和,当我拿到prefixSum[j]的值的时候，
                # 我去检查曾经是否有prefixSum[j]-k也就是prefixSum[i]出现过，如果出现过，就说明存在从prefixSum[i]到prefixSum[j]的距离为k的情况
                # 那么这个曾经是否出现过要如何判断呢，当然是hash,这也是下面那个解法的思路
                # table保存啦。那如何更新这个hash
                # table呢，当然是每次获得一个prefixSum，就存进去，如果表里没有这个key，那么value设置为1，否则value += 1


                prefixsum += nums[j]
                if prefixsum == k:
                    count += 1


# 前缀和+哈希表,复杂度为O(N),学到了,这个好难想啊,学不会
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Hash = {0: 1}
        numSum = 0
        res = 0

        for i in range(len(nums)):
            numSum += nums[i]
            res += Hash.get(numSum - k, 0)
            Hash[numSum] = Hash.get(numSum, 0) + 1

        return res


b = [2, 3, 0, 0, 5, 0]

a = Solution().subarraySum(b, 5)
print(a)
