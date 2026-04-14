class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1

        seen = sorted(seen, key= seen.get, reverse=True)

        return seen[:k]