class Solution:
    def searchInsert(self, nums, target):
        for i, n in enumerate(nums):
            if n >= target: return i
        return len(nums)

