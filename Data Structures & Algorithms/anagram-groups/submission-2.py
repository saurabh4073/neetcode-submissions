class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for word in strs:
            count = [0] * 26 #for 26 characters
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagramDict[tuple(count)].append(word)
        return list(anagramDict.values()) 

        