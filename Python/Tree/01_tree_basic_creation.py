class Node:

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    

class Tree:
    def __init__(self,root, name = "" ):
        self.root = root
        self.name = name


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

print(f'My {myTree.name} Data: \n')

print(f"         {myTree.root.data}")
print("         /\\")
print(f"     {myTree.root.left.data}      {myTree.root.right.data}")
print("     /\\      /\\")
print(f"   {myTree.root.left.left.data}  {myTree.root.left.right.data}  {myTree.root.right.left.data}  {myTree.root.right.right.data}")

