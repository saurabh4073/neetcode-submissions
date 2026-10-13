class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = defaultdict(list)

        for s in strs:
            cOrd = [0]*26
            for c in s:
                cOrd[ord(c)-ord('a')] +=1
            hashm[tuple(cOrd)].append(s)
        # print(hashm)
        res = []
        for key,val in hashm.items():
            res.append(val)
        # print(res)
        return res
