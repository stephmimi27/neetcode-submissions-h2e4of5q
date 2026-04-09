class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r: 
            half = l + (r - l)//2 #halfway point is the space we allow

            if nums[half] < nums[r]: #the middle is less than the right everything is
                r = half
            else: 
                l = half + 1 #otherwise check rightside
        return nums[l]