class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        for h in range(len(heights)-1):
            for i in range(len(heights)-1, 0, -1):
                a = (i - h) * min(heights[h], heights[i])
                if a > max:
                    max = a
        return max