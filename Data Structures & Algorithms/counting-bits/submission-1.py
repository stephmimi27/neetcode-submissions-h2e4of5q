class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []

        for i in range(n+1):
            a = self.numBits(i)
            res.append(a)
        return res

        

    def numBits(self, n: int) -> int:

        r = 0

        while n:
            n &= n - 1
            r += 1
        
        return r
        
