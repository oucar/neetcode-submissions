from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        c = sorted(Counter(nums))
        
        maxSequence = 1
        highest = 1

        for i in range(1, len(c)):
            if c[i] == c[i-1] + 1:
                maxSequence += 1
                highest = max(highest, maxSequence)
            else: 
                maxSequence = 1
        return highest
        