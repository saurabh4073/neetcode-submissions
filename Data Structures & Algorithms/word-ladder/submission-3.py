class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patternmap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j] + "*" + word[j+1:]
                patternmap[pattern].append(word)
        
        visit= set([beginWord])
        q=deque([beginWord])
        transform=1
        while q:
            for i in range(len(q)):
                word= q.popleft()
                if word==endWord:
                    return transform
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for nei in patternmap[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            transform+=1
        return 0
