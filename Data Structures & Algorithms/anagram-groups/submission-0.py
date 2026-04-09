class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s: #character in string
                count[ord(c) - ord('a')] += 1 #gives each charcter a val count
            res[tuple(count)].append(s)
        return list(res.values())
