class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderPrint(root):
    if root:
        inOrderPrint(root.left)
        print(root.val)
        inOrderPrint(root.right)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

inOrderPrint(root)
