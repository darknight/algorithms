class Solution(object):
    def v1canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #Time Limit Exceeded
        length = len(gas)
        if length == 0:
            return -1
        if length == 1:
            return 0
        gas = gas + gas
        cost = cost + cost
        index = -1
        for i in range(length):
            found = True
            tmp = 0
            j = i+1
            while j - i <= length:
                tmp = tmp + gas[j-1] - cost[j-1]
                if tmp < 0:
                    found = False
                    break
                else:
                    j += 1
            if found:
                index = i
                break
        return index

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #TODO: slow & improve
        length = len(gas)
        if length == 0:
            return -1
        if length == 1:
            if gas[0] >= cost[0]:
                return 0
            return -1
        gas = gas + gas
        cost = cost + cost
        index = -1
        i = 0
        while i < length:
            found = True
            tmp = 0
            j = i+1
            while j - i <= length:
                tmp = tmp + gas[j-1] - cost[j-1]
                if tmp < 0:
                    found = False
                    i = j
                    break
                else:
                    j += 1
            if found:
                index = i
                break
        return index

if __name__ == '__main__':
    print Solution().canCompleteCircuit([1,2,3,5], [2,3,4,3])
