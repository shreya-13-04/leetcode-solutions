class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        result=[]
        for i in range(n):
            if nums[i]<target:
                result.append(nums[i])
            else:
                result.append(target)
        for i in range(len(result)):
            if result[i]==target:
                return i
        return n

        
                
        