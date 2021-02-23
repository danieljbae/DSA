class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def binaryInsert(self, root,newNode):
        if root is None:
            root = newNode
        else: # determine if newNode belongs left or right subtree
            if newNode.val < root.val:
                if not root.left: # found open spot
                    root.left = newNode
                else:
                    self.binaryInsert(root.left,newNode)
            else:
                if not root.right: # found open spot
                    root.right = newNode
                else:
                    self.binaryInsert(root.right,newNode)

def inOrderPrint(root):
    if root:
        inOrderPrint(root.left)
        print(root.val)
        inOrderPrint(root.right)

root = TreeNode(4)
root.binaryInsert(root,TreeNode(12))
root.binaryInsert(root,TreeNode(1))
root.binaryInsert(root,TreeNode(7))
root.binaryInsert(root,TreeNode(3))
root.binaryInsert(root,TreeNode(8))

inOrderPrint(root)
