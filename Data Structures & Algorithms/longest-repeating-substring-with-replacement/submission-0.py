class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_freq = 0
        max_length = 0

        for r in range(len(s)):
            # 1. Expand the window by adding the current character
            count[s[r]] += 1
            
            # 2. Track the most frequent character in the current window
            max_freq = max(max_freq, count[s[r]])

            # 3. Check if the window is valid:
            # (Window Length - Most Frequent Char Count) = number of chars to replace
            if (r - l + 1) - max_freq > k:
                # If invalid, shrink the window from the left
                count[s[l]] -= 1
                l += 1
            
            # 4. Update the best result we've seen so far
            max_length = max(max_length, r - l + 1)
 
        return max_length