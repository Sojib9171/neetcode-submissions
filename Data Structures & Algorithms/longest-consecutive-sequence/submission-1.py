from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_lcs_length=0
        for i in range(len(nums)):
          step=1
          j=0
          while j<len(nums):

            if nums[j]==nums[i]+step:
              print('in')
              step=step+1
              j=0
            else:
              j=j+1

          if step> longest_lcs_length:
            longest_lcs_length=step

        return longest_lcs_length

