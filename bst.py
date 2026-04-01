class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self._inorder(self.root, []))

    def insert(self, val):
        def helper(node):
            if not node:
                return TreeNode(val)
            if node.val > val:
                node.left = helper(node.left)
            else:
                node.right = helper(node.right)
            return node
        
        self.root = helper(self.root)
    
    def delete(self, val):
        def helper(node, v):
            if not node:
                return
            if node.val > v:
                node.left = helper(node.left, v)
            elif node.val < v:
                node.right = helper(node.right, v)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    succ = self._min(node.right)
                    node.val = succ.val
                    node.right = helper(node.right, succ.val)
            return node
        
        self.root = helper(self.root, val)

    def find(self, val):
        def helper(node):
            if not node:
                return False
            if node.val == val:
                return True
            elif node.val > val:
                return helper(node.left)
            else:
                return helper(node.right)
        
        return helper(self.root)

    def _min(self, T):
        def helper(node):
            if not node:
                return
            return helper(node.left) or node
        return helper(T)
    
    def _inorder(self, T, ret):
        if not T:
            return []
        self._inorder(T.left, ret)
        ret.append(T.val)
        self._inorder(T.right, ret)
        return ret


if __name__ == '__main__':
    bst = BST()
    print("TEST INSERT")
    bst.insert(10)
    bst.insert(-10)
    bst.insert(-2)
    bst.insert(-6)
    bst.insert(-5)
    print("BST:", bst)
    print("TEST DELETE")
    bst.delete(-6)
    bst.delete(-5)
    print("BST:", bst)
    print("TEST FIND")
    print("Is 10 in BST?:", bst.find(10))
    print("Is -1 in BST?:", bst.find(-1))
