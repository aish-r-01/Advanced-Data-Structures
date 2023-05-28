class node:
    def __init__(self,item=None,parent=None,left=None,right=None):
        self.value=item
        self.parent=parent
        self.left=left
        self.right=right
        
class bst():
    def __init__(self):
        self.root = None
        self.size = 0

    def isleaf(self,pos):
        return pos.left==None and pos.right==None
        
    def find(self,key,pos=None):         #key-to be searched and pos->from where we shld search
        if pos==None:
            pos=self.root
        if pos.value == key:
            return pos
        elif pos.value > key:       #searching in left side
            if pos.left is not None:
                return self.find(key,pos.left)
        elif pos.value < key:
            if pos.right is not None:
                return self.find(key,pos.right)
            
        return pos
    
    def insert(self,value):         #value to be inserted
        if self.root == None:
            self.root = node(value)
            self.size+=1
            
        pos = self.find(value)
        if pos.value > value:
            if pos.left is None:
                new=node(value)
                pos.left = new
                new.parent = pos
                self.size+=1
        elif pos.value < value:
            if pos.right is None:
                new=node(value)
                pos.right = new
                new.parent = pos
                self.size+=1
            
    def preorder(self,root):
        if root is not None:
            print(root.value)
            self.preorder(root.left) 
            self.preorder(root.right)
    def getmin(self,pos):
        if pos is None or pos.left is None:
            return pos
        return self.getmin(pos.left)

    def delete(self,pos):    
        if self.isleaf(pos):
            if pos.parent.left==pos:
                pos.parent.left=None
            else:
                pos.parent.right=None
        elif pos.left!=None and pos.right==None:
            if pos.parent.left==pos:
                pos.parent.left=pos.left
            else:
                pos.parent.right=pos.left
        elif pos.right!=None and pos.left==None:
            if pos.parent.left==pos:
                pos.parent.left=pos.right
            else:
                pos.parent.right=pos.right
        else:
            m=self.getmin(pos.right)
            self.delete(m)
            pos.value=m.value
        self.size-=1

    def nearestval(self,target,pos=1):
        if pos==1:
            pos=self.root
        val=pos.value
        if target<val:
            nextpos=pos.left
        else:
            nextpos=pos.right
        if not nextpos:
            return val
        val2=self.nearestval(target,nextpos)
        return min((val,val2),key=lambda x:abs(target-x))

#function call       
t=bst()
l=[8,12,10,5,7,1]
for i in l:
    t.insert(i)
print("Nearest element for 14:")
print(t.nearestval(14))
