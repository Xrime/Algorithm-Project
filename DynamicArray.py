class DynamicArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range")
        return self.array[i]

    def insert(self, i, val):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of range")
        self.array[i] = val

    def add(self, val):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = val
        self.size += 1

    def remove(self):
        if self.size == 0:
            raise IndexError("Array is empty")
        self.size -= 1
        return self.array[self.size]

    def resize(self):
        new_capacity = 2 * self.capacity
        new_array = [0] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

    def to_list(self):
        return self.array[:self.size]

    def display(self):
        print(self.to_list())

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self.size)
            return [self.array[i] for i in range(start, stop, step)]
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def __iter__(self):
        for i in range(self.size):
            yield self.array[i]

    def clear(self):
        self.size = 0

    def extend(self, iterable):
        for value in iterable:
            self.add(value)

    def copy(self):
        clone = DynamicArray(self.capacity)
        clone.size = self.size
        clone.array[:self.size] = self.array[:self.size]
        return clone

    def __repr__(self):
        return f"DynamicArray({self.to_list()})"
