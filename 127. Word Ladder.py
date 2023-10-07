from typing import List
import collections, math, string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isAdjacent(word1, word2):
            count = 0
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    count += 1
            return count == 1
        
        def genNeighbor(word):
            word = list(word)
            neighbors = []
            for i in range(len(word)):
                originChar = word[i]
                for char in string.ascii_lowercase:
                    if char == originChar:
                        continue
                    word[i] = char
                    neighbors.append("".join(word))
                word[i] = originChar
            return neighbors

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # wordSet.add(beginWord)
        
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, dist = queue.popleft()
            for neighbor in genNeighbor(word):
                if neighbor == endWord:
                    return dist + 1
                if neighbor in wordSet:
                    queue.append((neighbor, dist + 1))
                    wordSet.remove(neighbor)
        return 0

soln = Solution()
print(soln.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
