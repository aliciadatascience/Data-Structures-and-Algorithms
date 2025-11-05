#inorder: left, node, right
# definition for a binary tree node:
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# recursion
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        def helper(node):
            #if node is null, using 'if not node'
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)
        return res

 # iterative
class solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res

