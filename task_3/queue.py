class Queue:

    def __init__(self):
        self._list_queue = []

    def push(self, x):
        self._list_queue.append(x)

    def pop(self):
        x = self._list_queue[0]
        del(self._list_queue[0])
        return x

    def top(self):
        return self._list_queue[-1]

    def size(self):
        return len(self._list_queue)

    def is_empty(self):
        return self._list_queue == []

    def clear(self):
        self._list_queue = []


a = Queue()
a.push(10)
a.push(20)
a.push(100)
a.push('q')
print(a.pop())
print(a.size())
print(a.is_empty())
print(a.top())
a.clear()
print(a.is_empty())



