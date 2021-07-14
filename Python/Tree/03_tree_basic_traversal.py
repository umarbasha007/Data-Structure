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


#Basic Creation

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


#Search target Data

foundNode  = myTree.search(75)
print(f"{foundNode.data}")


# Tree Traversal

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


