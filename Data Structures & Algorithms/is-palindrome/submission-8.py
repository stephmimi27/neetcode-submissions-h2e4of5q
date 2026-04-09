class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")

        new = []

        for char in s:
            if char.isalnum():
                char = char.lower()
                new.append(char)
        
        return new == new[::-1]
        