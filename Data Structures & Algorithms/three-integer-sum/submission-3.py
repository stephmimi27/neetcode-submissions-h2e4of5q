class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums = sorted(nums)

        for i, a in enumerate(nums): 
            if a > 0: #if the val is greater break 
                break

            if i > 0 and a == nums[i - 1]: #after the first round 
                continue 
                #the value is equal to the one before 
                #skip as already covered

            #left pointer and right pointer
            l, r = i + 1, len(nums) - 1  

            #as they reach each other
            while l < r: 
                threeSum = a + nums[l] + nums[r] #a plus 3 potential values
                if threeSum > 0: #if result is greater than zero go smaller
                    r -= 1
                elif threeSum < 0: #if less than zero go bigger
                        l += 1
                else: #if fine
                    res.append([a, nums[l], nums[r]]) #append together and move values forward
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: #if the value is the same
                        l += 1

        return res