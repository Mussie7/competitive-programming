class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = ''
        for i in t:
            if i in s:
                s = s.replace(i, "", 1)
            else:
                ans = i

        return ans
