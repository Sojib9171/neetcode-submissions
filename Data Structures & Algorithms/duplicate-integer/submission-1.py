class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        dups=[]
        for i in nums:
            if i in dict:
              dict[i]+=1
            else:
              dict[i]=1
        for key,value in dict.items():
          if value>1:
            dups.append(key)
        if len(dups)>0:
          return True
        else:
          return False