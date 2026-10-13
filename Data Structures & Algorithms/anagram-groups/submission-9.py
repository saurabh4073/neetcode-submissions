class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = defaultdict(list)

        for s1 in strs:
            count = [0]*26
            for s in s1:
                count[ord(s)-ord('a')]+=1
            list1[tuple(count)].append(s1)
        return list(list1.values())