from typing import List

#执行用时：40 ms, 在所有 Python3 提交中击败了99.88%的用户
#内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.57%的用户
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        min_len = float('inf')
        min_str = A[0]
        for i in A:
            if len(i)<min_len:
                min_len = len(i)
                min_str = i
        A.remove(min_str)
        self.A = A
        self.res = []
        self.mem = {}
        def valid(s):
            for st in self.A:
                if s not in st:
                    self.mem[s] = 1
                    break
            else:
                self.res.append(s)
                self.A = [st.replace(s, '',1)for st in self.A]


        for s in min_str:
            if s in self.mem:
                continue
            valid(s)

        return self.res

a=Solution().commonChars(["dbaabcba","cabcdbab","bdddddaa"])
print(a)