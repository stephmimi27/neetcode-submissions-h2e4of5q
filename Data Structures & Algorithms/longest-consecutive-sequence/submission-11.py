class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(set(nums)) 
        counter = 1
        res = 1

        if nums == []:
            return 0 

        for num in nums:
            if (num + 1) in nums:
                counter += 1
            else:
                res = max(res, counter)
                counter = 1
                
        return max(res, counter)