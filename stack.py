class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None;


class Stack:
    def __init__(self):
        self.stack = None
        self.front = None
        self.elem_count = 0
        self.read_only = False

    def __repr__(self):
        arr = []
        curr = self.front

        while curr:
            arr.append(curr.val)
            curr = curr.next

        return str(arr)

    def stack_size(self):
        return self.elem_count
    
    def push(self, value):

        assert not self.read_only

        new_node = ListNode(value)

        if (self.stack_size == 0):
            self.stack = new_node
        else:
            new_node.next = self.front
        
        self.front = new_node
        self.elem_count += 1

    def pop(self):

        assert not (self.read_only or self.stack_size == 0)

        curr = self.front

        self.front = curr.next
        self.elem_count -= 1

        return curr

    def lock(self):
        self.read_only = True
    
    def unlock(self):
        self.read_only = False

    def is_locked(self):
        return self.read_only


s = Stack()
s.push(10)
s.push(11)
s.push(-9)
s.push(10)

print("Stack is:", s) # [10, -9, 11, 10]

s.pop()

print("Stack is:", s) # [-9, 11, 10]

s.pop()

print("Stack is:", s) # [11, 10]

s.lock()

print("Is stack locked?", s.is_locked()) # true

try:
    s.pop()
except AssertionError:
    print("Can't modify stack. Stack is locked")

s.unlock()

print("Is stack locked?", s.is_locked()) # false

s.pop()

print("Stack is:", s) # [10]