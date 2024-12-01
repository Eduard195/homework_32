class Mylist:
    def __init__(self, l : list):
        self.l = l

    def copy(self):
        l1 = self.l
        return l1

    def append(self, x):
        self.l.append(x)

    def pop(self, ind = -1):
        return self.l.pop(ind)

    def index(self, v):
        return self.l.index(v)
    
    def count(self, v):
        return self.l.count(v)
    
    def insert(self, i, v):
        self.l.insert(i, v)

    def remove(self, v):
        self.l.remove(v)

    def sort(self):
        self.l.sort()

    def __str__(self):
        return str(self.l)
    

l = Mylist([1, 4, 6, 2, 8, 5])

l1 = l.copy()

l.append(1)
print(l.pop())
l.sort()
print(l)