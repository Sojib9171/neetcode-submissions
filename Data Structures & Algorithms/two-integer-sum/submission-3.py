class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={value: index for index, value in enumerate(nums)}
        print(d)
        for index, number in enumerate(nums):
          if d.get(target-number) == index:
            continue
          if target-number in d:
            return [index, d.get(target-number)]