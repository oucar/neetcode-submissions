from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            # Split word into characters and sort alphabetically
            chars = sorted(list(word))
            # Join back into a string key
            key = "".join(chars)
            # Add word to its group
            groups[key].append(word)
        
        return list(groups.values())