class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = " ".join(s)
        b = []
        for c in s: 
            if c.isalnum():
                c = c.lower()
                b.append(c)
        
        return b == b[::-1]
