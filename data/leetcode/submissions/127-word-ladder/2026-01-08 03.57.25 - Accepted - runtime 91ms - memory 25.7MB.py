class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList=[beginWord]+wordList

        adj_map=defaultdict(list)
        pref_map=defaultdict(set)
        suff_map=defaultdict(set)
        M=len(wordList)
        N=len(beginWord)
        if N==1: return 2*(endWord in wordList)

        for i in range(N):
            for j,word in enumerate(wordList):
                if i>0: pref_map[word[:i]].add(j)
                if i<N-1: suff_map[word[i+1:]].add(j) 
     
        for i in range(N):
            for j,word in enumerate(wordList):
                if i==0:
                    adj_map[j].extend(list(suff_map[word[i+1:]]))
                elif i==N-1:
                    adj_map[j].extend(list(pref_map[word[:i]]))
                else:
                    adj_map[j].extend(list(pref_map[word[:i]] & suff_map[word[i+1:]]))
        startIdx=wordList.index(beginWord)
        q=deque([startIdx])
        seen={startIdx:1}

        while q:
            curr=q.popleft()
            count=seen[curr]
            for neighbor in adj_map[curr]:
                if neighbor in seen: continue
                seen[neighbor]=count+1
                q.append(neighbor)
                if wordList[neighbor]==endWord:
                    return seen[neighbor]
        return 0
