import os


class TextLoader:
    def __init__(self, value):
        self.value = value
        self.list = os.listdir(self.value)
        self.start = 0
        self.nxt = None

    def get_next(self):
        return self.nxt

    def get_value(self, i):
        file=self.list[i]
        way=self.value+'\\'+str(file)
        a=''
        with open(way, 'r', encoding='utf8') as f:
            for line in f:
                x = line.lower()
                symbols = ['!', '?', '.', ',', ':',  '(', ')', '-', '"', ';', '”', '–']
                for symbol in symbols:
                    if symbol in x:
                        x = x.replace(symbol, '')
                a += x + '\n'
        return a

    def __getitem__(self, idx):
        if idx >= self.__len__():
            raise IndexError("Index out of range")
        return self.get_value(idx)


    def __len__(self):
        return len(os.listdir(self.value))

    def __iter__(self):
        self.index = self.start
        return self

    def __next__(self):
        if self.index is None or self.index >= self.__len__():
            raise StopIteration()
        val = self.get_value(self.index)
        self.index += 1
        return val

my_dir=os.getcwd()+'\\sample'
elem = TextLoader(my_dir)
for i in elem:
    print(i)
print(len(elem))