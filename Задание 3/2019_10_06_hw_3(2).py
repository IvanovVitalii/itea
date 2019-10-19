class Stack:

    def __init__(self):
        self._list_stack = []

    def push(self, x):
        self._list_stack.append(x)

    def pop(self):
        x = self._list_stack[-1]
        del(self._list_stack[-1])
        return x

    def get_size(self):
        return len(self._list_stack)

    def is_empty(self):
        return self._list_stack == []

    def del_stack(self):
        self._list_stack = []


a = Stack()
a.push(10)
a.push(20)
a.push(100)
a.push('q')
print(a.pop())
print(a.get_size())
print(a.is_empty())
a.del_stack()
print(a.is_empty())



