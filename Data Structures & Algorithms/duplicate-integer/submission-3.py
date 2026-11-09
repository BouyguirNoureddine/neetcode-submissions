class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set(nums)
        if len(cache) == len(nums):
            return False
        
        return True