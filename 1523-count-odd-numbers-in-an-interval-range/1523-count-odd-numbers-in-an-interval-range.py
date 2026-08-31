class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length=(high-low)+1
        
        if length%2==0:
            return length//2
        return length//2+low%2
        