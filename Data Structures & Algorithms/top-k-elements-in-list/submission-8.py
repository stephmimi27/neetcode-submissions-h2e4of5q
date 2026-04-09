class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        res = defaultdict(int)

        for n in nums:
            res[n] += 1

        res = sorted(res, key=res.get, reverse=True)

        return res[:k]