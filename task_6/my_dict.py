class Dict(dict):

    def my_get(self, key):
        a = 0
        for i in self:
            if i == key:
                a = self[i]
                break
            else:
                a = None
        return a

    def my_items(self):
        a = []
        for i in self:
            a += [(i, self[i])]
        return a

    def my_keys(self):
        a = []
        for i in self:
            a += [i]
        return a

    def my_values(self):
        a = []
        for i in self:
            a += [self[i]]
        return a

    def my_update(self, other):
        for i in other:
            if i not in self.my_keys():
                self[i] = other[i]
        return self

    def __add__(self, other):
        a = Dict()
        a.my_update(self)
        a.my_update(other)
        return a


d1 = Dict()
print(d1)
d2 = {a: a ** 2 for a in range(5)}
print(d2.values())
d1.my_update(d2)
d2 = {'s' * a: a * 2 for a in range(1, 4)}
d3 = Dict()
d3.my_update(d2)
print(type(d1))
print(type(d3))
print(d1[2])
print(d1.my_get(2))
print(d1.my_items())
print(d1.my_keys())
print(d1.my_values())
print(d1 + d3)
print(d1.my_update(d3))