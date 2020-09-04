
#1. 为什么需要每次移动短板? 2. 假如目前边界是[i,j],且li[i]<li[j], 为什么移动i不会丢失以i为挡板的最大面积?
#这个解释非常的好: https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
# 若不指定移动规则，所有移动出现的S(i, j) 的状态数为 C(n, 2)即暴力枚举出所有状态
# 在状态 S(i, j)下向内移动短板至 S(i + 1, j)（假设 h[i] < h[j] ），则相当于消去了 {S(i, j - 1), S(i, j - 2), ... , S(i, i + 1)}的
# 状态集合。而所有消去状态的面积一定 <= S(i, j
# 学到了,时间O(n),空间O(1)
class Solution:
    def maxArea(self, li) -> int:
        l, r = 0, len(li) - 1
        ans = 0
        while l < r:
            area = min(li[l], li[r]) * (r - l)
            ans = max(ans, area)
            if li[l] > li[r]:
                r -= 1
            else:
                l += 1
        return ans


# 自己写的暴力法,复杂度为O(N**2),会超出时间限制
class Solution:
    def maxArea(self, li) -> int:

        max_area = 0
        for i in range(len(li) - 1):
            for j in range(i, len(li)):
                max_area = max(max_area, (j - i) * min(li[i], li[j]))
        return max_area

5
a = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(a)
