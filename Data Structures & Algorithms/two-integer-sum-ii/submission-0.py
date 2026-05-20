class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length=len(numbers)
        left_p=0
        right_p=length-1

        while left_p<right_p:
          sum=numbers[left_p]+numbers[right_p]
          if sum == target:
            return [left_p+1, right_p+1]

          if sum > target:
            right_p-=1
          
          if sum < target:
            left_p+=1

        return [left_p+1, right_p+1]
