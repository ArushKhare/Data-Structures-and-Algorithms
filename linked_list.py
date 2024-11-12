class Node(object):
    def __init__(self, value, next): # O(1)
        self.value = value
        self.next = next
    
    def __eq__(self, other): # O(1)
        return (other.value == self.value)
    
    def __str__(self): # O(1)
        return str(self.value)

class LinkedList:
    def __init__(self): # O(1)
        self.root = None
        self.end = None
        self.size = 0
    
    def add_value(self, value): # O(1)
        new_node = Node(value, None)
        if not self.root:
            self.root = new_node
        else:
            self.end.next = new_node
        
        self.end = new_node
        self.size += 1
    
    def add_node(self, node): # O(1)
        if not self.root:
            self.root = node
        else:
            self.end.next = node
        self.end = node
        self.size += 1

    def remove_all(self, value): # O(size)
        # Empty Linked List
        if not self.root:
            return
        # Only the root and root is not equal to value
        if self.size == 1:
            if self.root.value != value:
                return
        # Delete the root if it is the value
        if self.root.value == value:
            self.root = self.root.next
            self.size -= 1
            return
        # For all other values
        prev = self.root
        curr = self.root.next
        while curr:
            if curr.value == value:
                if curr == self.end:
                    self.end = prev
                prev.next = curr.next
                curr = prev.next
                self.size -= 1
            else:
                prev = curr
                curr = curr.next
    
    def pop(self, index): # O(size)
        assert index >= 0 and index < self.size

        if index == 0:
            value = self.root.value
            self.root = self.root.next
            self.size -= 1
            return value

        current_index = 0
        prev = None
        current = self.root

        while current_index < index:
            prev = current
            current = current.next
            current_index += 1
        
        value = current.value
        if current == self.end:
            self.end = prev
        prev.next = current.next
        self.size -= 1
        return value
    
    def get_size(self): # O(1)
        return self.size
    
    def to_array(self): # O(size)
        current = self.root
        array = []
        while current:
            array.append(current.value)
            current = current.next
        return array
    
    def sort(self, reverse=False): # O(size^2)
        # Using Bubble Sort
        if self.root:
            sorted = False
            while not sorted:
                current = self.root
                sorted = True
                while (current.next):
                    if current.value > current.next.value:
                        sorted = False
                        temp = current.value
                        current.value = current.next.value
                        current.next.value = temp
                    current = current.next
                current = self.root
        
        if reverse:
            self.reverse()
    
    def get_value_at(self, index): # O(size)
        assert index >= 0 and index < self.size

        current_index = 0
        current = self.root

        if (index == self.size):
            return self.end.value

        while current_index < index:
            current = current.next
            current_index += 1
        
        return current.value
    
    def get_node_at(self, index): # O(size)
        assert index >= 0 and index < self.size

        current_index = 0
        current = self.root

        if (index == self.size):
            return self.end

        while current_index < index:
            current = current.next
            current_index += 1
        
        return current
    
    def reverse(self): # O(size)
        if (self.size <= 1):
            return
        prev = self.root
        curr = self.root.next
        while (curr):
            prev.next = curr.next
            curr.next = self.root
            self.root = curr
            curr = prev.next
        self.end = prev
            
    def merge(self, other): # O(1)
        self.add_node(other.root)
        # add_node() makes size 1 more than actual size. Subtract the size by 1 to fix error.
        self.size += other.size - 1
    
    def __str__(self): # O(size)
        return str(self.to_array())


lList = LinkedList()
lList.add_value(10)
lList.add_value(2)
lList.add_value(4)
lList.add_value(4)
lList.add_value(4)
lList.add_value(18)

print(lList)
lList.remove_all(4)
print(lList)

lList.add_value(19)
lList.add_value(16)
print(lList)

lList.sort(reverse=True)
print(lList)

lList.pop(3)
print(lList)

lList2 = LinkedList()
lList2.add_value(11)
lList2.add_value(20)

lList.merge(lList2)
print(lList)

lList.sort()
print(lList)
