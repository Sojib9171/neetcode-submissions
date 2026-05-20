class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lists=[]
        dist_tup=set()
        result=[]
        for i in range(0,len(nums)-2):
          for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
              if nums[i]+nums[j]+nums[k]==0:
                lists.append([nums[i],nums[j],nums[k]])

        for x in lists:
          x.sort()
          dist_tup.add(tuple(x))

        for t in dist_tup:
          result.append(list(t))


        return result