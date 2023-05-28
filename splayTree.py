
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:

    def __init__(self):
        self.root = None

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
            
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        
        if x.parent == None: #x is root
            self.root = y

        elif x == x.parent.left: #x is left child
            x.parent.left = y

        else: #x is right child
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None: #x is root
            self.root = y

        elif x == x.parent.right: #x is right child
            x.parent.right = y

        else: #x is left child
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, n):

        while n.parent != None: #node is not root

            if n.parent == self.root: #node is child of root, one rotation
                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)

            else:
                p = n.parent
                g = p.parent #grandparent

                if n.parent.left == n and p.parent.left == p: #both are left children
                    self.right_rotate(g)
                    self.right_rotate(p)

                elif n.parent.right == n and p.parent.right == p: #both are right children
                    self.left_rotate(g)
                    self.left_rotate(p)

                elif n.parent.right == n and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)

                elif n.parent.left == n and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)

    def insert(self, n):

        n = Node(n)

        y = None
        temp = self.root

        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y

        if y == None: #newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

        self.splay(n)

    def search(self, n, x):

        if x == n.data:
            self.splay(n)
            return n

        elif x < n.data:
            return self.search(n.left, x)
        elif x > n.data:
            return self.search(n.right, x)
        else:
            return None
        
    def __join(self, s, t):
        
        if s == None:
            return t

        if t == None:
            return s
        
        x = self.maximum(s)
        self.splay(x)
        x.right = t
        t.parent = x
        return x
    
    def __delete_node_helper(self, node, key):

        x = None
        t = None 
        s = None

        while node != None:
            if node.data == key:
                x = node
            if node.data <= key:
                 node = node.right
            else:
                node = node.left
                
        if x == None:
            print("Couldn't find key in the tree")
            return
        
        self.splay(x)

        if x.right != None:
            t = x.right
            t.parent = None
        else:
            t = None
            
        s = x
        s.right = None
        x = None


        if s.left != None:
            s.left.parent = None
            
        self.root = self.__join(s.left, t)
        s = None

    def delete(self, data):   
        self.__delete_node_helper(self.root, data)

    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            print(n.data, end="  ")
            self.inorder(n.right)

    def preorder(self, n):
        if n != None:
            print(n.data)
            self.preorder(n.left)
            self.preorder(n.right)

if __name__ == '__main__':
    tree = SplayTree()
    tree.insert(10)
    tree.insert(120)
    tree.insert(140)
    tree.insert(150)
    tree.insert(110)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(90)
    tree.insert(100)
    tree.insert(160)
    tree.insert(70)
    tree.search(tree.root, 160)
    tree.inorder(tree.root)
    print()
    print('root is')
    print(tree.root.data)