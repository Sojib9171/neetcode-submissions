class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        group_anagrams=[]
        for i in range(0, len(strs)):
            sorted_key=''.join(sorted(strs[i]))
            if sorted_key not in d:
                d[sorted_key]=[strs[i]]
            else:
                continue

            for j in range(i+1, len(strs)):
                if sorted_key==''.join(sorted(strs[j])):
                    d[sorted_key].append(strs[j])
        
        for value in d.values():
          group_anagrams.append(value)

        return group_anagrams