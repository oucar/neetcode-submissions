from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        # number, count 
        frequencies = c.most_common(k)

        result = []
        for number, count in frequencies:
            result.append(number)

        return result 
