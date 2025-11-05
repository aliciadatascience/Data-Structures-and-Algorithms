  
class Solution:
    def searchInsert(self, nums, target):
        if target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
