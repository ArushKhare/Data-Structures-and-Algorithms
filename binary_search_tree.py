class Node(object):
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def copy(self):
        return Node(self.val, self.left, self.right)
    
    def __str__(self):
        return str(self.val)

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def get_root_value(self):
        if not self.root:
            return
        return self.root.val
    
    def height(self):
        def height_helper(node):
            if not node:
                return 0
            return 1 + max(height_helper(node.left), height_helper(node.right))
        
        return height_helper(self.root)
    
    def tree_size(self):
        def size_helper(node):
            if not node:
                return 0
            return 1 + size_helper(node.left) + size_helper(node.right)
        
        return size_helper(self.root)
        
    
    def push(self, val) -> bool:
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return True
        curr = self.root
        while curr:
            if curr.val == val: 
                return False
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    break
            else:
                assert val < curr.val
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    break
        return True
    
    def remove(self, val) -> bool:
        if not self.root:
            return
        prev = None
        curr = self.root
        while curr:
            if curr.val > val:
                prev = curr
                curr = curr.left
            elif curr.val < val:
                prev = curr
                curr = curr.right
            else:
                assert curr.val == val
                # If node is leaf
                if not curr.left and not curr.right:
                    if (prev.left == curr): 
                        prev.left = None
                    elif (prev.right == curr):
                        prev.right = None
                    return True
                # If node only has right child
                if not curr.left:
                    if prev.left == curr:
                        prev.left = curr.right
                    else:
                        prev.right = curr.right
                    return True
                # If node only has left child
                if not curr.right:
                    if prev.right == curr:
                        prev.right = curr.left
                    else:
                        prev.left = curr.left
                    return True
                # If node has both children
                if curr.left and curr.right:
                    temp = curr.right
                    prev = curr
                    while temp.left:
                        prev = temp
                        temp = temp.left
                    curr.val = temp.val
                    # This happens if curr.right had a left-child
                    if prev.left == temp:
                        prev.left = temp.right
                    # This happens if curr.right had no left-child
                    if prev.right == temp:
                        prev.right = temp.right
                    temp = None
                    return True
        return False

    def preorder_traversal(self) -> list:
        if not self.root:
            return
        arr = []
        def preorder_helper(root):
            if not root: return
            arr.append(root.val)
            preorder_helper(root.left)
            preorder_helper(root.right)
        preorder_helper(self.root)
        return arr
    
    def inorder_traversal(self) -> list:
        if not self.root:
            return
        arr = []
        def inorder_helper(root):
            if not root: return
            inorder_helper(root.left)
            arr.append(root.val)
            inorder_helper(root.right)
        inorder_helper(self.root)
        return arr
    
    def postorder_traversal(self) -> list:
        if not self.root:
            return
        arr = []
        def postorder_helper(root):
            if not root: return
            postorder_helper(root.left)
            postorder_helper(root.right)
            arr.append(root.val)
        postorder_helper(self.root)
        return arr
    
    def level_order_traversal(self) -> list:
        if not self.root:
            return
        from collections import deque
        arr = []
        queue = deque()
        queue.append(self.root)
        while (queue):
            curr = queue.popleft()
            arr.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return arr
    
    def find_path(self, val):
        if not self.root:
            return
        path = ""
        curr = self.root
        while curr:
            if curr.val == val:
                return path
            elif curr.val > val:
                curr = curr.left
                path += 'l'
            else:
                assert curr.val < val
                curr = curr.right
                path += 'r'
        return ""
    
    def check_existence(self, val):
        if not self.root:
            return
        curr = self.root
        while curr:
            if curr.val == val:
                return True
            elif curr.val > val:
                curr = curr.left
            else:
                assert curr.val < val
                curr = curr.right
        return False


bst = BinarySearchTree()

bst.push(10)
bst.push(-19)
bst.push(20)
bst.push(15)
bst.push(12)
bst.push(17)

print("17 in BST:", bst.check_existence(17))
print("Path to 17:", bst.find_path(17))

print("BST Height:", bst.height())
print("BST Node Count:", bst.tree_size())

print("Inorder Traversal:", bst.inorder_traversal())
print("Preorder Traversal:", bst.preorder_traversal())
print("Postorder Traversal:", bst.postorder_traversal())
print("Level Order Traversal:", bst.level_order_traversal())

print("Removed 10:",bst.remove(10))
print("Inorder Traversal:", bst.inorder_traversal())

print("Root:", bst.get_root_value())

print("Removed 15:", bst.remove(15))
print("Removed 17:", bst.remove(17))

print("17 in BST:", bst.check_existence(17))

print("Inorder Traversal:", bst.inorder_traversal())
