class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        counter = 0
        l = 0

        for r in range(len(s)):

            while s[r] in seen:
                
                seen.remove(s[l])
                l += 1
            
            
            seen.add(s[r])
            counter = max(counter, r - l + 1) #this is the window of space
        return counter