class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        comparator = nums[:]
        comparator.sort()
        start, end, checker = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] != comparator[i]:
                start = i
                checker = 1
                break
                
        if not checker:
            return 0
            
        for j in range(-1, -len(nums)-1, -1):
            if nums[j] != comparator[j]:
                end = j
                break
        
        return len(nums) + end - start + 1
