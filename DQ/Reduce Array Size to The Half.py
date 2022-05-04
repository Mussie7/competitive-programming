from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        frequency = c.most_common()
        sum = frequency[0][1]
        count = 1
        for i in range(1, len(c)):
            if sum >= len(arr)//2:
                break
            else:
                sum += frequency[i][1]
                count += 1
        
        return count
