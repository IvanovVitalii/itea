class List(list):

    def my_append(self, value):
        self += [value]

    def my_pop(self, index=-1):
        a = self[index]
        del self[index]
        return a

    def my_clear(self):
        self = []
        return self

    def my_len(self):
        a = 0
        for i in self:
            a += 1
        return a

    def my_remove(self, value):
        a = 0
        for i in range(self.my_len()):
            if self[i] != value:
                a += 1
            elif self[i] == value:
                del self[i]
                break
        if a == self.my_len():
            raise ValueError

    def __add__(self, other):
        for i in other:
            self += [i]
        return self


l1 = List()
l2 = List()
l1.my_append(111)
l1.my_append(11)
l1.my_append(12)
l1.my_append(11)
l1.my_append(11)
l1.my_append(10)
print(l1)
l2.my_append(12)
l2.my_append(1)
print(l2)
l3 = l1 + l2
print(l3)
print(l3.my_len())
print(l3.my_pop())
print(l3.my_pop(5))
print(l3)
l3.my_remove(11)
print(l3)
print(l1.my_clear())