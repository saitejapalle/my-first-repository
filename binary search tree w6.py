class Node:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        ctr=0
        node=Node(data)
        if self.root==None:
            self.root=node
        else:
            temp=self.root
            while True:
                if data<temp.data and temp.l is None:
                    temp.l=node
                    break
                if data>temp.data and temp.r is None:
                    temp.r=node
                    break
                if data<temp.data and temp.l!=None:
                    temp=temp.l
                if data>temp.data and temp.r!=None:
                    temp=temp.r
            print("Node inserted")
            ctr+=1
    def searching(self,root,n):
        if n==root.data:
            print("Element found",root.data)
            return
        elif n>root.data:
            if self.root.r is not None:
                self.searching(root.r,n)
            else:
                return "No match found"
        else:
            if self.root.l is not None:
                self.searching(root.l,n)
            else:
                return "Element not found"
    def postorder(self,root):
        if root:
            self.postorder(root.l)
            self.postorder(root.r)
            print(root.data)
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.l)
            self.preorder(root.r)
    def inorder(self,root):
        if root:
            self.inorder(root.l)
            print(root.data)
            self.inorder(root.r)
    def leafnode(self,root):
        if root:
            self.leafnode(root.l)
            self.leafnode(root.r)
            if root.l == None and root.r==None:
                print(root.data)
    def height(self,root):
        if root==None:
            return -1
        else:
            return 1+max(self.height(root.l),self.height(root.r))
    def nleafnode(self,root):
        if root:
            self.nleafnode(root.l)
            self.nleafnode(root.r)
            if root.l != None and root.r != None:
                print(root.data)

    def minValueNode(node):
        current = node
        while(current.left is not None):
            current = current.l
        return current 
    def deleteNode(self,root,key):
        if root is None:
            return root
        if key < root.key:
            root.l = self.deleteNode(root.l,key)
        elif(key > root.key):
            root.right =self.deleteNode(root.r,key)
        else:
            if root.l is None :
                temp = root.r
                root = None
                return temp
            elif root.r is None :
                temp = root.l
                root = None
                return temp
            temp = minValueNode(root.r)
            root.key = temp.key
            root.r =self.deleteNode(root.r,temp.key)
        return root

b=BST()
print("******************TREE USING DOUBLE LINKED LIST************************")
while True:
    print("1.Insertion \n2.Post Order Traversal\n3.Pre Order Traversal")
    print("4.In Order Traversal\n5.Leaf Node of Tree\n6.Height of Tree\n7.Non-Leaf Node")
    print("8.Searching\n9.Deleting\n10.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
          data=eval(input("Enter data:"))
          b.insert(data)
    elif ch==2:
        b.postorder(b.root)
    elif ch==3:
        b.preorder(b.root)
    elif ch==4:
        b.inorder(b.root)
    elif ch==5:
        b.leafnode(b.root)
    elif ch==6:
        print(b.height(b.root))
    elif ch==7:
        b.nleafnode(b.root)
    elif ch==8:
        n=eval(input("Enter search element:"))
        b.searching(b.root,n)
    elif ch==9:
        data=eval(input("Enter delete element:"))
        b.deleteNode(b.root,data)
        print(data,"Deleted")
    else:
        print("Exit")
        break
