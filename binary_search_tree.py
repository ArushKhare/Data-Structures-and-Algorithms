class Node(object):
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    
    def __str__(self):
        return str(self.val)

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def push(self, val) -> bool:
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return True
        curr = self.root
        while curr:
            if curr.val == val: 
                return False
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    break
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    break
        return True

    def preorder_traversal(self) -> list:
        assert self.root
        arr = []
        def preorder_helper(root):
            if not root: return
            arr.append(root.val)
            preorder_helper(root.left)
            preorder_helper(root.right)
        preorder_helper(self.root)
        return arr
    
    def inorder_traversal(self) -> list:
        assert self.root
        arr = []
        def inorder_helper(root):
            if not root: return
            inorder_helper(root.left)
            arr.append(root.val)
            inorder_helper(root.right)
        inorder_helper(self.root)
        return arr
    
    def postorder_traversal(self) -> list:
        assert self.root
        arr = []
        def postorder_helper(root):
            if not root: return
            postorder_helper(root.left)
            postorder_helper(root.right)
            arr.append(root.val)
        postorder_helper(self.root)
        return arr
    
    def level_order_traversal(self) -> list:
        assert self.root
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
        assert self.root
        path = ""
        curr = self.root
        while curr:
            if curr.val == val:
                return path
            if curr.val > val:
                curr = curr.left
                path += 'l'
            if curr.val < val:
                curr = curr.right
                path += 'r'
        return ""
    
    def check_existence(self, val):
        assert self.root
        curr = self.root
        while curr:
            if curr.val == val:
                return True
            if curr.val > val:
                curr = curr.left
            if curr.val < val:
                curr = curr.right
        return False


bst = BinarySearchTree()
bst.push(10)
bst.push(-19)
bst.push(20)
bst.push(15)
bst.push(12)
bst.push(17)
print("Inorder Traversal:", bst.inorder_traversal())
print("Preorder Traversal:", bst.preorder_traversal())
print("Postorder Traversal:", bst.postorder_traversal())
print("Level Order Traversal:", bst.level_order_traversal())
