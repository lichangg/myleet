#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 重点题型
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
# 本质找到两个数组合起来后第k小的数
from typing import List





# 这个方法的复杂度还是O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        i = 0  # 循环次数
        pre = None  # 前一个弹出的数，length为偶数会用到
        cur = None
        # 之前总是想着维护一个记录索引累加的变量count,然后i一直循环,当count等于中位数时退出,那可真是太蠢了
        # 实际上只需要像下面这样, i只循环到中位数索引就行,退出后result自然就是中位数索引对应的值(不过还需要维护一个pre变量,当总数是偶数时用得到)
        # 而且这个顺序还是从后往前,这样pop的效率会高,学到了
        while i < length // 2 + 1:
            n1 = nums1[-1] if nums1 else -float('inf')
            n2 = nums2[-1] if nums2 else -float('inf')
            pre = cur
            cur = nums1.pop() if n1 > n2 else nums2.pop()
            i += 1
        result = cur
        if length % 2 == 0:
            result = (result + pre) / 2
        return result

# 直接用归并法合并一下,不过这样复杂度是O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        num = self.merge(nums1, nums2)
        print(num)
        div, mod = divmod(len(num), 2)
        if not mod:
            return (num[div] + num[div - 1]) / 2
        else:
            return num[div]

    def merge(self, num1, num2):
        res = []
        i, j = 0, 0
        n1 = len(num1)
        n2 = len(num2)
        while i <= n1 - 1 and j <= n2 - 1:
            if num1[i] < num2[j]:
                res.append(num1[i])
                i += 1
            else:
                res.append(num2[j])
                j += 1
        res += num1[i:]
        res += num2[j:]
        return res

# 上面两个方法都达不到要求的复杂度.
# 由于两数组有序,所以不用一个一个排除它是不是中位数,而是可以一次性排除比它小的所有数,也即是二分查找的思想
# 时间复杂度：每进行一次循环，我们就减少 k/2 个元素，所以时间复杂度是 O(log(k))，而 k=(m+n)/2，所以最终的复杂也就是 O(log(m+n））。
# A 数组中比 A [ k / 2 ] 小的数有 k / 2 - 1 个，B 数组中，B [ k / 2 ] 比 A [ k / 2 ] 大，
# 假设 B [ k / 2 ] 前边的数字都比 A [ k / 2 ] 小，也只有 k / 2 - 1 个，所以比 A [ k / 2 ] 小的数字最多有 k / 2 - 1 + k / 2 - 1 = k - 2 个，
# 所以 A [ k / 2 ] 最多是第 k - 1 小的数。而比 A [ k / 2 ] 小的数更不可能是第 k 小的数了，所以可以把它们排除。
def helper(nums1, nums2, k):
    # 这一步很精髓,学到了
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1  # 保持nums1比较长
    if len(nums2) == 0:
        return nums1[k - 1]  # 短数组空，直接返回
    if k == 1:
        return min(nums1[0], nums2[0])  # 找最小数，比较数组首位
    t = min(k // 2, len(nums2))  # 保证不上溢
    if (nums1[t - 1] >= nums2[t - 1]):
        return helper(nums1, nums2[t:], k - t)
    else:
        return helper(nums1[t:], nums2, k - t)

num1 = [1,3]
num2 = [2]

a=Solution().findMedianSortedArrays(num1,num2)
print(a)
