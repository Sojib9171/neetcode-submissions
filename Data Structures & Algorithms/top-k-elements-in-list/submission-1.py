from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      counter=dict()

      for n in nums:
        if n in counter:
          counter[n]=counter[n]+1
        else:
          counter[n]=1

      freq_group=dict()
      for i in range (len(nums)+1):
        freq_group[i]=[]

      for key,value in counter.items():
        freq_group[value].append(key)

      result=[]
      for key, value in reversed(freq_group.items()):
        if len(freq_group[key])==0:
          continue
        result.extend(freq_group[key])

      return result[0:k]
