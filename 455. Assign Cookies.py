from typing import *
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count_child = 0
        g.sort()
        s.sort()
        i, j = 0, 0
        print(g)
        print(s)
        while i <= len(g)-1 and j <= len(s)-1:
            if g[i] <= s[j]:
                s.pop(j)
                count_child += 1
                i += 1
            else:
                j += 1

        return count_child



sol = Solution()
g = [10,9,8,7]
s = [5,6,7,8]

print(sol.findContentChildren(g, s))