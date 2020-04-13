# Binary Search Tree
# Access: logn
# Search: 


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    node = Node(val)

    if root.val is None:
        root.val = val
    else:
        if node.val > root.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, val)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, val)


def printInorder(root): 
  
    if root:
        printInorder(root.left) 
        print(root.val)
        printInorder(root.right) 
  
def printPostorder(root): 

    if root:
        printPostorder(root.left) 
        printPostorder(root.right) 
        print(root.val)
  
def printPreorder(root): 

    if root:
        print(root.val)
        printPreorder(root.left) 
        printPreorder(root.right) 


def search(root, val):
    # search for a value in the three
    if root is None or root.val == val:
        return root

    if root.val < val:
        return search(root.right, val)
    else:
        return search(root.left, val)

if __name__ == '__main__':

    root = Node()

    insert(root, 10)
    insert(root, 1)
    insert(root, 5)
    insert(root, 3)
    insert(root, 9)
    printInorder(root)


    for val in [4, 1, 5, 7, 10, 14]:
        node = search(root, val)
        if node is None:
            print(f"Could not find {val} in the binary tree")
        else:
            print(f"Found value {node.val} in the tree")


    # print("Prinding in order transversal")
    #printInorder(root)

    # print("Printing post order transversal")
    # printPostorder(root)

    # print("Printing pre order transversal")
    # printPreorder(root)

