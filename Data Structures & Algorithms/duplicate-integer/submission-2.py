class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for n in nums:
            seen.add(n)

        if len(seen)==len(nums):
            return False

        return True