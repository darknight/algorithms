#!/usr/bin/env python3

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #TODO: slow, improve
        if numCourses <= 0:
            return False
        if numCourses == 1:
            return True
        degree = [0] * numCourses
        adj_list = [[] for _ in xrange(numCourses)]
        for pre in prerequisites:
            j, i =  pre
            adj_list[i].append(j)
            degree[j] += 1
        while True:
            found = False
            for i, d in enumerate(degree):
                if d == 0:
                    numCourses -= 1
                    found = True
                    break
            if not found:
                break
            for v in adj_list[i]:
                degree[v] -= 1
            degree[i] -= 1

        return numCourses == 0

if __name__ == '__main__':
    print(Solution().canFinish(2, [[1,0]]))
    print(Solution().canFinish(2, [[1,0],[0,1]]))
