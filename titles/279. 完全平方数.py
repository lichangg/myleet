#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math


# 思路: dp_nums的索引代表要求的数,其值为和为该数的平方数的最小个数
# 执行用时：6180 ms, 在所有 Python3 提交中击败了12.48%的用户
# 内存消耗：14 MB, 在所有 Python3 提交中击败了36.01%的用户
class Solution:
    def numSquares(self, n: int) -> int:
        # 学到了,我先根据n生成好可能的平方数
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp_nums = [float('inf') for _ in range(n + 1)]
        for index in range(n + 1):
            for sq in square_nums:
                if sq > index:
                    break

                if index == sq:
                    dp_nums[index] = 1
                    # 不做这一步的优化就会超时
                    break
                else:
                    # dp_nums[index - sq] + 1 这个逻辑很精髓
                    dp_nums[index] = min(dp_nums[index - sq] + 1, dp_nums[index])
        print(dp_nums)
        return dp_nums[n]

# 贪心算法,真是精妙啊,学到了
# 对于给定的n, 从组合数最小(也就是1)开始找起,
#   1. 如果没有, 则找组合数是2的, 还没有的话以此循环
#       1. 对于单次循环来说, count逐渐-1递归的找,在递归过程中若是找到了,则表明此count可行(因为迭代顺序是由小变大,所以这就是最小count了)
class Solution:
    def numSquares(self, n):

        def is_divided_by(n, count):
            """
                return: true if "n" can be decomposed into "count" number of perfect square numbers.
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count


# 贪心 + BFS（广度优先搜索）
# 这个就是由目标数(也即是根)遍历减去square_nums里面的数,得到第一层各子节点, 各子节点再遍历减去square_nums里面的数,直到得到某个子节点的值也在square_nums里面,该子节点所在的层数就是最小组合数了
class Solution:
    def numSquares(self, n):

        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            # ! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level

a = Solution().numSquares(13)
print(a)
