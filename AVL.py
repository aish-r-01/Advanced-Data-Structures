class node:
    def __init__(self,val):
        self._val=val
        self._left=None
        self._right=None
        self.height=1

class AVLtree:
    def insert(self,root,val):
        if not root:
            return node(val)
        elif val<root._val:
            root._left=self.insert(root._left,val)
        else:
            root._right=self.insert(root._right,val)
        root.height=1+max(self.height1(root._left),self.height1(root._right))
        bal=self.balance(root)
        if bal>1 and val<root._left._val:
            return self.rightrotate(root)
        if bal<-1 and val>root._right._val:
            return self.leftrotate(root)
        if bal>1 and val>root._left._val:
            root._left=self.leftrotate(root._left)
            return self.rightrotate(root)
        if bal<-1 and val<root._right._val:
            root._right=self.rightrotate(root._right)
            return self.leftrotate(root)
        return root

    def delete(self,root,val):
        if not root:
            return root
        elif val<root._val:
            root._left=self.delete(root._left,val)
        elif val>root._val:
            root._right=self.delete(root._right,val)
        else:
            if root._left is None:
                d=root._right
                root=None
                return d
            elif root._right is None:
                d=root._left
                root=None
                return d
            d=self.getmin(root._right)
            root._val=d._val
            root._right=self.delete(root._right,d._val)
        if root is None:
            return root
        root.height=1+max(self.height1(root._left),self.height1(root._right))
        bal=self.balance(root)
        if bal>1 and self.balance(root._left)>=0:
            return self.rightrotate(root)
        if bal<-1 and self.balance(root._right)<=0:
            return self.leftrotate(root)
        if bal>1 and self.balance(root._left)<0:
            root._left=self.leftrotate(root._left)
            return self.rightrotate(root)
        if bal<-1 and self.balance(root._right)>0:
            root._right=self.rightrotate(root._right)
            return self._leftrotate(root)
        return root

    def leftrotate(self,p):
        right=p._right
        left=right._left
        right._left=p
        p._right=left
        p.height=1+max(self.height1(p._left),self.height1(p._right))
        right.height=1+max(self.height1(right._left),self.height1(right._right))
        return right

    def rightrotate(self,p):
        left=p._left
        right=left._right
        left._right=p
        p._left=right
        p.height=1+max(self.height1(p._left),self.height1(p._right))
        left.height=1+max(self.height1(left._left),self.height1(left._right))
        return left

    def getmin(self,r):
        if r is None or r._left is None:
            return r
        return self.getmin(r._left)

    def height1(self,r):
        if not r:
            return 0
        return r.height

    def balance(self,r):
        if not r:
            return 0
        return self.height1(r._left)-self.height1(r._right)

    def inorder(self,s):
        if  s is None:
            return
        #i=[]
        self.inorder(s._left)
        print(s._val)
        self.inorder(s._right)

    def preorder(self,r):
        if not r:
            return
        print(r._val)
        self.preorder(r._left)
        self.preorder(r._right)

    def postorder(self,k):
        if not k:
            return
        self.postorder(k._left)
        self.postorder(k._right) 
        print(k._val)

    def arraysorted(self,lst):
        if not lst:
            return None
        m=len(lst)//2
        Node=node(lst[m])
        Node._left=self.arraysorted(lst[:m])
        Node._right=self.arraysorted(lst[m+1:])
        return Node
    

lst=[1,2,3,4,5]
a=AVLtree()
r=a.arraysorted(lst)

print("Preorder:")
a.preorder(r)

print("Inorder:")
a.inorder(r)

print("Postorder:")
a.postorder(r)

