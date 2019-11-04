class Stack:

    def __init__(self):
        self._list_stack = []

    def push(self, x):
        self._list_stack.append(x)

    def pop(self):
        x = self._list_stack[-1]
        del(self._list_stack[-1])
        return x

    def size(self):
        return len(self._list_stack)

    def top(self):
        return self._list_stack[0]

    def is_empty(self):
        return self._list_stack == []

    def clear(self):
        self._list_stack = []


a = Stack()
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



