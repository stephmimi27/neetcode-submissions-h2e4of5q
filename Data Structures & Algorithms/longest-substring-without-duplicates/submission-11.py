class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #already seen
        res = 0 #returned
        l = 0
        count = 0

        if len(s) == 1:
            return 1
        if len(s) < 1:
            return 0

        for r in range(len(s)): #for every character in s
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r - l + 1)
 
        return res


        