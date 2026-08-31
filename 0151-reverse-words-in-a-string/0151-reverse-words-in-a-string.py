class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right=len(s)-1
        
        word=s.split()
        word.reverse()
        return " ".join(word)
        