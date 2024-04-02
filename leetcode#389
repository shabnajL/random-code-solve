### leetcode 389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #return s, t
        cnt = 0
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        for i in (s):
            if t.count(i) > s.count(i):
                return i
                break
        return t[len(t)-1]
