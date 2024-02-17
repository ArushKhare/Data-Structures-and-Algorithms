class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __eq__(self, other):
        return (other.value == self.value)
    
    def __str__(self):
        return str(self.value)

class LinkedList:

    def __init__(self):
        self.root = None
        self.size = 0
    
    def add_value(self, value):
        if not self.root:
            self.root = Node(value, None)
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = Node(value, None)
        self.size += 1
    
    def add_node(self, node):
        if not self.root:
            self.root = node
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def remove_first_instance(self, value):
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
        # For all other values
        prev = self.root
        curr = self.root.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                self.size -= 1
                break
            prev = curr
            curr = curr.next
    
    def pop(self, index):
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
        prev.next = current.next
        self.size -= 1
        return value
    
    def get_size(self):
        return self.size
    
    def to_array(self):
        current = self.root
        array = []
        while current:
            array.append(current.value)
            current = current.next
        return array
    
    def sort(self, reverse=False):
        # Using Bubble Sort
        if self.root:
            sorted = False
            while not sorted:
                current = self.root
                sorted = True
                for i in range(self.size-1):
                    if current.value > current.next.value:
                        sorted = False
                        temp = current.value
                        current.value = current.next.value
                        current.next.value = temp
                    current = current.next
                current = self.root
        
        if reverse:
            self.reverse()
    
    def get_value_at(self, index):
        assert index >= 0 and index < self.size

        current_index = 0
        current = self.root

        while current_index < index:
            current = current.next
            current_index += 1
        
        return current.value
    
    def get_node_at(self, index):
        assert index >= 0 and index < self.size

        current_index = 0
        current = self.root

        while current_index < index:
            current = current.next
            current_index += 1
        
        return current
    
    def reverse(self):
        for i in range(self.size // 2):
            node1 = self.get_node_at(i)
            node2 = self.get_node_at(self.size-1-i)
            
            temp = node1.value
            node1.value = node2.value
            node2.value = temp

    def merge(self, other):
        self.add_node(other.root)
        # add_node() makes size 1 more than actual size. Subtract the size by 1 to fix error.
        self.size += other.size - 1
    
    def __str__(self):
        return str(self.to_array())


lList = LinkedList()
lList.add_value(10)
lList.add_value(2)
lList.add_value(4)
lList.add_value(4)
#lList.remove_first_instance(4)
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
