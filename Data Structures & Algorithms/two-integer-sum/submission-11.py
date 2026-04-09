class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique = {}

        for i in range(len(nums)):

            if target - nums[i] in unique:
                return [unique[target - nums[i]], i]
            unique[nums[i]] = i