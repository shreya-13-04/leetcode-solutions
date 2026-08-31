class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count=0
        n=len(nums)
        result={}
        for i in range(n):
            if nums[i] in result:
               if i-result[nums[i]]<=k:
                return True
            result[nums[i]]=i

        return False