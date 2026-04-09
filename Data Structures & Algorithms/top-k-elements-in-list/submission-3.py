class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1

        while k > 0:
            a = max(count, key=count.get)
            res.append(a)
            del count[a]       
            k -=1
        
        return res

                
