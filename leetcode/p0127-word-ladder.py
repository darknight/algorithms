#!/usr/bin/env python3
from time import time
from time import time_ns

class Solution(object):
    from typing import List
    #
    # TLE
    #
    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        for word in wordList:
            if self.connected(beginWord, word):
                break
        queue = [beginWord]
        visited = set()
        res = 0
        while len(queue) > 0:
            res += 1
            tmp_queue = []
            for word in queue:
                if word == endWord:
                    return res
                visited.add(word)
                for next_word in wordList:  # slow
                    if next_word not in visited and self.connected(word, next_word):
                        tmp_queue.append(next_word)
            queue = tmp_queue
        return 0

    #
    # TLE
    #
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        for word in wordList:
            if self.connected(beginWord, word):
                break
        queue = [beginWord]
        nonvisited = set(wordList)
        res = 0
        while len(queue) > 0:
            res += 1
            tmp_queue = []
            for word in queue:
                if word == endWord:
                    return res
                nonvisited.discard(word)
                for next_word in nonvisited:
                    if self.connected(word, next_word):
                        tmp_queue.append(next_word)
            queue = tmp_queue
        return 0

    #
    # TLE
    #
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        if endWord not in wordList:
            return 0
        for word in wordList:
            if self.connected(beginWord, word):
                break
        queue = [beginWord]
        map = defaultdict(list)
        visited = set([beginWord])
        res = 0

        if beginWord not in wordList:
            wordList.append(beginWord)
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if self.connected(wordList[i], wordList[j]):
                    map[wordList[i]].append(wordList[j])
                    map[wordList[j]].append(wordList[i])
        while len(queue) > 0:
            print(queue)
            res += 1
            tmp_queue = []
            for word in queue:
                if word == endWord:
                    return res
                visited.add(word)
            for word in queue:
                for next_word in map[word]:
                    if next_word not in visited:
                        visited.add(next_word)
                        tmp_queue.append(next_word)
            queue = tmp_queue
        return 0

    #
    # TLE
    # but Java version can pass
    #
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        for word in wordList:
            if self.connected(beginWord, word):
                break
        wordList.append(beginWord)

        cnt = 0
        graph = []
        for i in range(len(wordList)):
            graph.append([])

        for i in range(len(wordList)-1):
            s = time()
            for j in range(i+1, len(wordList)):
                if self.connected(wordList[i], wordList[j]):
                    cnt += 1
                    graph[i].append(j)
                    graph[j].append(i)

        res = 0
        target = wordList.index(endWord)
        queue = [len(wordList) - 1]
        visited = [False] * len(wordList)
        while len(queue) > 0:
            res += 1
            tmp_queue = []
            for index in queue:
                if index == target:
                    return res
                visited[index] = True
            for index in queue:
                for next_index in graph[index]:
                    if visited[next_index] is False:
                        visited[next_index] = True
                        tmp_queue.append(next_index)
            queue = tmp_queue
        return 0

    def connected(self, word1, word2) -> bool:
        cnt = 0
        for i in range(len(word1)):
            if cnt > 1:
                return False
            if word1[i] != word2[i]:
                cnt += 1
        return cnt == 1

if __name__ == '__main__':
    assert Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert Solution().ladderLength("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 6