#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
# 学到了,这方法比并查集还好用
#题目要求复杂度是O(n),下面这个方法有for还有while为什么也符合O(n)呢?
#解释: 如果有 x-1那么就不用做了,直接下一位,无论排序如何, 例如 [1,2,3] 只会做1的while 2,3的while都不会做, 再比如[2,1,3] 仍然也只做1的while而不会做2,3的while
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            # 如果这一步没跳出,那就可以保证当前得到的连续序列是以他开始
            if num - 1 in s:
                continue
            curLen = 1
            while num + 1 in s:
                curLen += 1
                num += 1
            res = max(res, curLen)
        return res



import collections

# 并查集
# 1. 初始化N个树节点,此时他们之间无法联通,所以其根节点都是自己
# 2. 遍历数组开始按规则合并, 合并的时候需要用到查找
class DSU:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.cnt = collections.defaultdict(lambda: 1) # 初始化默认字典, 学到了
        # print(self.pre,self.cnt)
    #不进行路径压缩
    # def find(self, x):
    #     while x != self.parent[x]:
    #         x = self.parent[x]
    #     return x

    def find(self, x):
        while x != self.parent[x]:
            # 路径压缩
            self.parent[x] = self.parent[self.parent[x]]

            x = self.parent[x]
        return x

    def union(self, x, y):
        if y not in self.parent:
            return 1
        # 寻找x, y的根节点，记为root1, root2
        root1, root2 = self.find(x), self.find(y)

        # 如果root1 == root2，直接返回self.cnt[root1]或者self.cnt[root2]
        # 表示当前的数与之前已经出现的一些数字能构成连续序列
        if root1 == root2:
            return self.cnt[root1]

        # 将root2的根节点改为root1，如下面步骤5中的图所示，将两棵子树合并
        self.parent[root2] = root1
        # 如下面步骤5中的图所示，两棵子树合并时，现在的树的元素个数就是这两棵树之和
        self.cnt[root1] += self.cnt[root2]
        return self.cnt[root1]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        dsu = DSU(nums)
        res = 1
        for num in nums:
            # print(num)
            res = max(res, dsu.union(num, num + 1))
            # print(dsu.pre,dsu.cnt,res)
        return res

# 二刷失败， 好好看看上面的几个解法，非常精妙
a=Solution().longestConsecutive([5,6, 1, 2, 3,4])
print(a)