# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#    *
#   / \
#  +    +
# / \  / \
#3  2  4  5
#You should return 45, as it is (3 + 2) * (4 + 5).


# Class to represent the nodes of syntax tree 
class node: 
    def __init__(self, val: int): 
        self.left = None
        self.val = val 
        self.right = None
  
# This function receives a node of the syntax tree 
# and recursively evaluate it 
def evaluateExpressionTree(root): 
  
    # empty tree 
    if root is None: 
        return 0
  
    # leaf node 
    if root.left is None and root.right is None: 
        return int(root.val) 
  
    # evaluate left tree 
    left_sum = evaluateExpressionTree(root.left) 
  
    # evaluate right tree 
    right_sum = evaluateExpressionTree(root.right) 
  
    # check which operation to apply 
    if root.val == '+': 
        return left_sum + right_sum 
      
    elif root.val == '-': 
        return left_sum - right_sum 
      
    elif root.val == '*': 
        return left_sum * right_sum 
      
    else: 
        return left_sum / right_sum 
  
# Driver function to test above problem 
if __name__=='__main__': 
      
    # creating a sample tree 
    root = node('*') 
    root.left = node('+') 
    root.left.left = node('3') 
    root.left.right = node('2') 
    root.right = node('+') 
    root.right.left = node('4') 
    root.right.right = node('5') 
    print(evaluateExpressionTree(root))
