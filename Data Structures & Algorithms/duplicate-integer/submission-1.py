class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for i in nums:
            if i not in cache:
                cache[i] = 1
            else:
                return True
        return False