class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0

        nums = set(nums)
        for num in nums:
            if (num - 1) not in nums:
                length = 0
                while (num + length) in nums:
                    length += 1
                if length > max:
                    max = length
        return max
        

        

        