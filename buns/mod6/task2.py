class DoubleElement:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            result = tuple(self.lst[self.index:self.index + 2])
            self.index += 2
            return result
        else:
            raise StopIteration


dL = DoubleElement((1, 2, 3, 4))
for pair in dL:
    print(pair)

print()

dL = DoubleElement((1, 2, 3, 4, 5))
for pair in dL:
    print(pair)