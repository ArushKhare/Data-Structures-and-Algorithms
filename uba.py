"""
Note that this code implements Unbounded Arrays similar to how they are
implemented in C++ and Java. However, Python lists are unbounded arrays by 
definition. I wrote this code to give an idea of how unbounded arrays look 
like based on Python. In actuality, you do not need to write this code.
"""

class Unbounded_Array():
    def __init__(self, initial_capacity=10):
        self.array = [0 for i in range(initial_capacity)]
        self.capacity = initial_capacity
        self.end = 0
    
    def __repr__(self):
        return str(self.array[0:self.end])
    
    def is_empty(self):
        return self.end == 0
    
    def get_length(self):
        return self.end
    
    def get_capacity(self):
        return self.capacity
    
    def resize(self, new_size):
        new_array = [0 for i in range(new_size)]

        for i in range(self.get_length()):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_size
    
    def add(self, val):
        # Resizes if array is too small
        if (self.end == self.capacity):
            self.resize(2 * self.capacity + 1)

        self.array[self.end] = val
        self.end += 1

    def remove(self):
        assert not self.is_empty()

        self.end -= 1
        self.array[self.end] = 0

        # Resizes if array is too big
        if self.end <= (self.capacity // 4):
            self.resize(self.capacity // 2)

    def add_at_index(self, index, val):
        assert 0 <= index < self.end

        # Resizes if array is too small
        if (self.end == self.capacity):
            self.resize(2 * self.capacity + 1)

        for i in range(index, self.end):
            self.array[i+1] = self.array[i]
        
        self.array[index] = val
        self.end += 1
    
    def remove_at_index(self, index):
        assert 0 <= index < self.end and not self.is_empty()

        for i in range(index+1, self.end):
            self.array[i-1] = self.array[i]
        
        self.end -= 1
        self.array[self.end] = 0

        # Resizes if array is too big
        if self.end <= (self.capacity // 4):
            self.resize(self.capacity // 2)


uba = Unbounded_Array(2) # []

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)

uba.add(10) # [10]
uba.add(17) # [10, 17]

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)

uba.add(-14) # [10, 17, -14]

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)

uba.add(-14) # [10, 17, -14, -14]
uba.add(107) # [10, 17, -14, -14, 107]
uba.add(19) # [10, 17, -14, -14, 107, 19]

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)

uba.remove() # [10, 17, -14, -14, 107]
uba.remove() # [10, 17, -14, -14]
uba.remove() # [10, 17, -14]

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)

uba.remove() # [10, 17]

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)

uba.remove() # [10]

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)

uba.remove() # []

print("Capacity:", uba.get_capacity(), end=", ")
print("Array:", uba)