class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #initialize array res with nums size spots all set to 1
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix #product of left
            prefix *= nums[i] #all the numbers on the left

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

