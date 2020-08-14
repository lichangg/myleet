#!/usr/bin/env python
# -*- coding:utf-8 -*-
#这种方法始终会用到额外空间,而题目要求[原地]修改
# class Solution:
#     def nextPermutation(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         def get_str_list(s):
#             if len(s) == 1:
#                 return s
#             head = s[0]
#             sub = s[1:]
#             if sub==sorted(sub,reverse=True):
#                 if s == sorted(s,reverse=True):
#                     return sorted(s)
#                 for index,i in enumerate(sub):
#                     if (index+1==len(sub) and i > head) or s[index+1] < head:
#                         s[0], s[index+1] = s[index+1], s[0]
#                         sub=sorted(s[1:])
#                         sub.insert(0,s[0])
#                         return sub
#                 else:
#                     return sorted(s)
#             else:
#                 sub = get_str_list(sub)
#                 sub.insert(0, head)
#                 return sub
#         nums = get_str_list(nums)
#         print(nums)

#比较复杂,以后再看
# class Solution:
#     def nextPermutation(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         index = 0
#         for i in range(len(nums)-1, 0, -1):
#             if nums[i] > nums[i-1]:
#                 index = i
#                 break
#         if index == len(nums)-1:
#             nums[index], nums[index-1] = nums[index-1], nums[index]
#         elif index == 0:
#             self.Reverse(nums, 0, len(nums)-1)
#         else:
#             self.Reverse(nums, index, len(nums)-1)
#             for s in range(index, len(nums)):
#                 if nums[s] > nums[index-1]:
#                     nums[index-1], nums[s] = nums[s], nums[index-1]
#                     break
#     def Reverse(self, nums, start, end):
#         mid = (start+end+1) // 2
#         k = 0
#         for j in range(start, mid):
#             nums[j], nums[end-k] = nums[end-k], nums[j]
#             k += 1

#比较优雅,但不满足原地修改
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                return
        nums.sort()


# Solution().nextPermutation([1,2,3])
for i in range(7,0,-1):
    print(i)


