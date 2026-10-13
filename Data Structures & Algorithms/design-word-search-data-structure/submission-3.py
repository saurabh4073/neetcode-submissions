class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root= TrieNode()

    def addWord(self, word: str) -> None:
        curr= self.root

        for w in word:
            if w not in curr.children:
                curr.children[w]= TrieNode()
            curr= curr.children[w]
        curr.endOfWord=True

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            curr= root

            for i in range(j,len(word)):
                if word[i] == ".":
                    for c in curr.children.values():
                        if dfs(i+1,c):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr=curr.children[word[i]]
            return curr.endOfWord

        return dfs(0,self.root)
