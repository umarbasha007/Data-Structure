class Node:

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
    # Search Node present or not in Node
    def search(self,target_data):
        if self.data == target_data:
            print(f"{target_data} is found")
            return self
        
        elif self.left != None and self.data > target_data:
            return self.left.search(target_data)

        elif self.right != None and self.data < target_data:
            return self.right.search(target_data)

        else:
            print(f"{target_data} is not found")
            self.data = None
            return self

    #Traersal in Node

    # Pre-Order -> data, left, right
    # In-Order  -> left, data, right
    # Post-Order-> left, right, data 

    def preorderTraversal(self):

        print(self.data)

        if self.left:
            self.left.preorderTraversal()

        if self.right:
            self.right.preorderTraversal()


    def inorderTraversal(self):
        
        if self.left:
            self.left.inorderTraversal()

        print(self.data)

        if self.right:
            self.right.inorderTraversal()


    def postorderTraversal(self):
        
        if self.left:
            self.left.postorderTraversal()

        if self.right:
            self.right.postorderTraversal()

        print(self.data)


    def reversePreorderTraversal(self):

        print(self.data)

        if self.right:
            self.right.reversePreorderTraversal()

        if self.left:
            self.left.reversePreorderTraversal()


    def reverseInoderTraversal(self):

        if self.right:
            self.right.reverseInoderTraversal()

        print(self.data)

        if self.left:
            self.left.reverseInoderTraversal()


    def reversePostorderTraversal(self):
        
        if self.right:
            self.right.reversePostorderTraversal()

        if self.left:
            self.left.reversePostorderTraversal()

        print(self.data)

    #Height

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h 
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

    def height2(self, h=0):

        leftHeight = rightHeight = h
        if self.left:
            leftHeight = self.left.height2(h+1)

        if self.right:
            rightHeight = self.right.height2(h+1)
        
        return max(leftHeight, rightHeight)

    #List of Nodes at a given depth
    def getNodesAtDepth(self,depth, nodes = []):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        if self.right:
            self.right.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        return nodes


        

class Tree:
    def __init__(self,node, name = "" ):
        self.root = node
        self.name = name

    # Search Node present or not in Tree
    def search(self, target_data):
        return self.root.search(target_data)

    # Tree Traversals
    def preorderTreeTraversal(self):
        return self.root.preorderTraversal()

    def inorderTreeTraversal(self):
        return self.root.inorderTraversal()

    def postorderTreeTraversal(self):
        return self.root.postorderTraversal()

    def reversePreorderTreeTraversal(self):
        return self.root.reversePreorderTraversal()

    def reverseInorderTreeTraversal(self):
        return self.root.reverseInoderTraversal()

    def reversePostorderTreeTraversal(self):
        return self.root.reversePostorderTraversal()

    def height(self):
        return self.root.height()

    def height2(self):
        return self.root.height2()

    def getNodesAtDepth(self,depth):
        return self.root.getNodesAtDepth(depth)


#01 - Basic Creation

node = Node(50) #Root Node

node.left = Node(25)
node.right = Node(75)

node.left.left = Node(20)
node.left.right = Node(30)

node.right.left = Node(60)
node.right.right = Node(80)

myTree = Tree(node, "basic_tree")

#         50
#         /\
#     25      75
#     /\      /\
#   20  30  60  80     

print(f'\nMy {myTree.name} Data: \n')

print(f"         {myTree.root.data}")
print("         /\\")
print(f"     {myTree.root.left.data}      {myTree.root.right.data}")
print("     /\\      /\\")
print(f"   {myTree.root.left.left.data}  {myTree.root.left.right.data}  {myTree.root.right.left.data}  {myTree.root.right.right.data}")


#02 - Search target Data

foundNode  = myTree.search(75)
print(f"{foundNode.data}")


#03 - Tree Traversal

print("\n Pre-Order Tree Traversal \n")
myTree.preorderTreeTraversal()

print("\n In-Order Tree Traversal - Ascending Order BST\n")
myTree.inorderTreeTraversal()

print("\n Post-Order Tree Traversal \n")
myTree.postorderTreeTraversal()

print("\n Reverse Pre-Order Tree Traversal \n")
myTree.reversePreorderTreeTraversal()

print("\n Reverse In-Order Tree Traversal - Descending Order BST\n")
myTree.reverseInorderTreeTraversal()

print("\n Reverse Post-Order Tree Traversal \n")
myTree.reversePostorderTreeTraversal()


#04 - Height of Tree

tallTree = Tree(Node(50), 'A Very Tall Tree')
tallTree.root.left = Node(25)
tallTree.root.right = Node(75)
tallTree.root.left.left = Node(10)
tallTree.root.left.right = Node(35)
tallTree.root.left.right.left = Node(30)
tallTree.root.left.right.right = Node(42)
tallTree.root.left.left.left = Node(5)
tallTree.root.left.left.right = Node(13)
tallTree.root.left.left.left.left = Node(2)

print(f"\nTree - {tallTree.name} : Height \n")
print(tallTree.height())
print(tallTree.height2())


shortTree = Tree(Node(50), 'A Very Short Tree')

print(f"\nTree - {shortTree.name} : Height \n")
print(shortTree.height())
print(shortTree.height2())


#05 - All nodes at given depth

depth = 3
print(f"\n Nodes at depth - {depth} \n")
nodes = tallTree.getNodesAtDepth(depth)
print(nodes)
