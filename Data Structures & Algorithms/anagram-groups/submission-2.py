from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            
            chars = sorted(list(word))
            key = "".join(chars)
            groups[key].append(word)

        return list(groups.values())