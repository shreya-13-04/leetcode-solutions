class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        maxArea=0
        while left<right:
            width=right-left
            curr_height=min(height[left], height[right])
            area=curr_height*width
            maxArea=max(maxArea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
                
           
        return maxArea
    




