class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    d = {}
    for word in strs:
        sorted_key = ''.join(sorted(word))   # O(k log k)
        if sorted_key not in d:
            d[sorted_key] = []
        d[sorted_key].append(word)          

    return list(d.values())