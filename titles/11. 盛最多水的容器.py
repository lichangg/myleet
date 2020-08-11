class Solution:
    def maxArea(self, li) -> int:
        l, r = 0, len(li)-1
        ans=0
        while l < r:
            area = min(li[l], li[r]) * (r-l)
            ans = max(ans, area)
            if li[l] > li[r]:
                r -=1
            else:
                l+=1
        return ans

a=Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(a)