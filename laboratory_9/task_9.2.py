class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


    def __iter__(self):
        if self:
            if self.left:
                for elem in self.left:
                    yield elem
            yield self.value
            if self.right:
                for elem in self.right:
                    yield elem

class BinTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, value):
        elem = Node(value)
        if self.root:
            self._insert(elem, self.root)
        else:
            self.root = elem
        self.length += 1

    def _insert(self, elem, parent):
        if elem.value < parent.value:
            if parent.left:
                self._insert(elem, parent.left)
            else:
                parent.left = elem
        else:
            if parent.right:
                self._insert(elem, parent.right)
            else:
                parent.right = elem

    def __len__(self):
        return self.length

    def get(self, value):
        if self.root:
            res = self._get(value, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, value, parent):
        if not parent:
            return None
        elif parent.value == value:
            return parent
        elif value < parent.value:
            return self._get(value, parent.left)
        else:
            return self._get(value, parent.right)

    def __getitem__(self, value):
        return self.get(value)

    def __iter__(self):
      return self.root.__iter__()

lst = BinTree()
a=[5, 30, 2, 40, 25, 4]
for i in a:
    lst.insert(i)

for i in lst:
    print(i)