class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            
            a=min(nums)
            b=max(nums)
            while b:
                a, b = b, a%b
            return a
        result=arr[0]

        for i in range(n):
            result=gcd(result, nums[i])

        return result






        