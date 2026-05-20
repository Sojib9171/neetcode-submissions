class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
      freq_dict={}
      for i in nums:
        if i in freq_dict:
          freq_dict[i]+=1
        else:
          freq_dict[i]=1
          
      sorted_freq_dict=dict(sorted(freq_dict.items(), key=lambda item:item[1], reverse=True),)

      keys=list(sorted_freq_dict.keys())
      output_list=keys[:k]

      return output_list