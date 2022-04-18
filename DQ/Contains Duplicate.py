from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        check = c.most_common(1)
        if check[0][1] > 1:
            return True
        else:
            return False
