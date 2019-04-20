class LRUCache(object):
    #TODO: slow, improve
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.queue = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.cache[key]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.cache:
            if len(self.queue) < self.capacity:
                self.queue.insert(0, key)
            else:
                k = self.queue.pop()
                del self.cache[k]
                self.queue.insert(0, key)
        else:
            self.queue.remove(key)
            self.queue.insert(0, key)
        self.cache[key] = value

if __name__ == '__main__':
    pass
