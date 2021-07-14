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


class Tree:
    def __init__(self,node, name = "" ):
        self.root = node
        self.name = name

    # Search Node present or not in Tree
    def search(self, target_data):
        return self.root.search(target_data)



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


#Search target Data

foundNode  = myTree.search(36)
print(f"{foundNode.data}")

