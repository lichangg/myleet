#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 效率太低超时了
# class Solution:
#     def threeSum(self, nums:list):
#         res = []
#         for index1, i in enumerate(nums):
#             index2 = index1 + 1
#             for _ in range(len(nums) - index1 - 1):
#                 if 0-i-nums[index2] in nums[index2+1:]:
#                     temp = [i, nums[index2], 0 - i - nums[index2]]
#                     temp.sort()
#                     if temp not in res:
#                         res.append(temp)
#                 index2 += 1
#
#         return res

# 自己瞎写的排序+双指针的方法，复杂度O(N**2)看别人的题解好像最快也就这样了
# 执行用时：1372 ms, 在所有 Python3 提交中击败了15.34%的用户
# 内存消耗：16.3 MB, 在所有 Python3 提交中击败了53.96%的用户
# class Solution:
#     def threeSum(self, nums:list ,target=0):
#         res = []
#         nums.sort()
#         if len(nums) == 3:
#             if nums[0] + nums[1] + nums[2] == target:
#                 res = [nums]
#             return res
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             l=i+1
#             r = len(nums) - 1
#             while l < r:
#                 if nums[i] + nums[l] + nums[r] == target:
#                     res.append([nums[i], nums[l], nums[r]])
#                     while l<r and nums[l]==nums[l+1]:
#                         l+=1
#                     while l<r and nums[r]==nums[r-+1]:
#                         r-=1
#                     l += 1
#                     r -= 1
#                 elif nums[i] + nums[l] + nums[r] <target:
#                     l+=1
#                 else:
#                     r-=1
#
#         return res

# 别人的方法
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


# 再刷
# 深度搜素,超时
# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         self.res = []
#         def dfs(cur_sum, cur,path, begin, dis):
#             new_path = path[::]
#             new_path.append(cur)
#             cur_sum +=cur
#             if cur_sum == 0 and dis == 0:
#                 self.res.append(new_path)
#                 return
#             if cur_sum > 0 or dis<0:
#                 return
#             pre= None
#             for idx, i in enumerate(nums):
#                 if idx<=begin or pre == i:
#                     continue
#                 else:
#                     pre= i
#                     dfs(cur_sum, i, new_path, idx, dis-1)
#         #用一个pre变量记录是否和上一个元素一样, 当前的i不可和pre相同,否则会出现重复结果, 但是当前i可以作为pre的子节点
#         pre = None
#         for idx, i in enumerate(nums):
#             if i == pre:
#                 continue
#             else:
#                 pre =i
#                 dfs(0, i, [], idx, 2)
#
#         return self.res

# 再刷失败, 思路要是固定一个i,再双指针
class Solution:
    def threeSum(self, nums):
        nums.sort()
        i = 0
        j = len(nums) - 1
        self.res = []

        while i < j:
            pre_i = nums[i]
            pre_j = nums[j]
            diff = 0 - nums[i] - nums[j]
            third = None
            for idx, x in enumerate(nums[i + 1:j]):
                if x == diff:
                    third = idx + i + 1
                    break
                elif x > diff:
                    break
            if third:
                self.res.append([nums[i], nums[j], nums[third]])
            if diff > 0:
                while pre_i == nums[i]:
                    i += 1
            else:
                while pre_j == nums[j]:
                    j -= 1

        return self.res


# 再刷
class Solution:
    def threeSum(self, nums):
        res = []
        for i in nums:
            for j in nums:
                if -j - i in nums:
                    res.append((i, j, -i - j))
        return res

a = Solution().threeSum([-4, -1, -1, -1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 7])
print(a)
# a=[0, 1, -1]
# a.sort()
# print(a)
