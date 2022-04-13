class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2 = []
        for i in strs:
            strs2.append(["".join(sorted(i)), i])
        strs2.sort()
        ans = []
        while len(strs2) > 0:
            temp = strs2.pop(0)
            ans.append([temp[1]])
            for i in range(len(strs2)):
                if temp[0] == strs2[0][0]:
                    temp = strs2.pop(0)
                    ans[-1].append(temp[1])
                else:
                    break
        
        return ans   
