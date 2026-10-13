class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashdict = defaultdict(list)

        for word in strs:
            anagram_word = ''.join(sorted(word))
            hashdict[anagram_word].append(word)
        return list(hashdict.values())

        