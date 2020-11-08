# Binary Search Tree
# Access: logn
# Search:


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


# inserts on left if smaller than root
# and right if larger than root
def insert(root: Node, val: int):
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


def printInorder(root: Node):
    # Depth first transversal InOrder
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def printPostorder(root: Node):
    # Depth first transversal PostOrder
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)


def printPreorder(root: Node):
    # Depth first transversal PreOrder
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)


def search(root: Node, val:int):
    # search for a value in the three
    if root is None or root.val == val:
        return root

    if root.val < val:
        return search(root.right, val)
    else:
        return search(root.left, val)


if __name__ == "__main__":

    root = Node()

    insert(root, 1)
    insert(root, 2)
    insert(root, 3)
    insert(root, 4)
    insert(root, 5)

    print("Printing InOrder binary tree:")
    printInorder(root)

    print("Printing PostOrder binary tree:")
    printPostorder(root)

    print("Printing PreOrder binary tree:")
    printPreorder(root)

    for val in [4, 1, 5, 7, 10, 14]:
        node = search(root, val)
        if node is None:
            print(f"Could not find {val} in the binary tree")
        else:
            print(f"Found value {node.val} in the tree")
