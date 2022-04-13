class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            if "".join(sorted(i)) in anagram:
                anagram["".join(sorted(i))].append(i)
            else:
                anagram["".join(sorted(i))] = [i]
        
        return anagram.values()
