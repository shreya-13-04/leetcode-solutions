class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(n):
            for j in range(n-i-1):
                if(nums[j]>nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]




