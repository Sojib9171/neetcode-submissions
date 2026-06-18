from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      pref=[]
      roll_mul=1
      pref.append(roll_mul)
      for i in range(1, len(nums)):
        roll_mul=roll_mul * nums[i-1]
        pref.append(roll_mul)

      post=[0] * len(nums)
      roll_mul=1
      post[-1]=roll_mul

      for i in range(len(nums)-2, -1, -1):
        roll_mul=roll_mul * nums[i+1]
        post[i]=roll_mul


      result=[]
      for i in range(len(nums)):
        result.append(pref[i] * post[i])

      return result