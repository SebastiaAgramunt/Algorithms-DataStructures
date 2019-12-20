class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


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

if __name__ == '__main__':

	root = Node(1)

	root.left = Node(2)
	root.right = Node(3)

	root.left.left = Node(4)
	root.left.right = Node(5)

	root.right.right = Node(6)
	root.right.left = Node(7)

	print("Prinding in order transversal")
	printInorder(root)

	print("Printing post order transversal")
	printPostorder(root)

	print("Printing pre order transversal")
	printPreorder(root)