#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 非滑动窗口的解决办法,也挺好理解的
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 使用一个辅助变量来暂时存储匹配的子串
#         ans = ''
#         tep = ''
#         for i in s:
#             # 遍历，若不重复则记录该字符
#             if i not in tep:
#                 tep += i
#             # 如果遇到了已经存在的字符，则找到该字符所在位置，删除该字符，并保留该位置之后的子串，并把当前字符加入到最后，完成更新
#             else:
#                 tep = tep[tep.index(i)+1:]
#                 tep += i
#             # 如果是当前最长的，就替换掉之前存储的最长子串
#             if len(tep) > len(ans):
#                     ans = tep
#         return len(ans)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap = {}
        res=0
        k=-1
        for index, i in enumerate(s):
            if i in hashmap and hashmap[i] > k:
                k = hashmap[i]
            else:
                res = max(res, index-k)
            hashmap[i] = index
        return res
# 自己写的,和上面的思路差不多都是滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j,start = 0,0
        max_len = 0
        hashmap = {}
        # 此处纠结了好久,在例如s='pwcwpdfc',当右针遇到s[3]时左针会收缩至s[2],没问题,但是当右针到s[4]时,你总不能把左针弄到s[1]吧(hashmap里面有了s[0])
        # 由于start会更新,所以可以加这个条件hashmap.get(s[j], 0)<start,也就是即便hashmap里面有了某字符,但是只要满足该条件也能表示没遇到重复的
        while j < len(s):
            if s[j] not in hashmap or hashmap.get(s[j], 0)<start:
                max_len = max(j-start+1, max_len)
            else:
                start = hashmap.get(s[j])+1
            hashmap[s[j]] = j
            j += 1

        return max_len


a=Solution().lengthOfLongestSubstring('dd')
print(a)