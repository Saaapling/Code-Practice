from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    """
        Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan&id=level-3
        Comments:
            - Initial Thoughts: Recurse Down, reconstruct tree going up
                - What if instead of reconstructing, you built tree as you go down?
                    - Update preorder as you go
                    - Use an index + array_math to keep track of / insert nulls?
                - Example: [3,9,20,15,7], [9,3,15,20,7]
                - Preorder: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
                    - Initial thoughts got the pro-order definition wrong :/
            - Revised Thoughts:
                - Build Left First
                - Still use recursion
                
    """
    
    def buildTreeAux_Left(self, inorder, head):
        if not self.preorder:
            return None
        
        curr = self.preorder[0]
        
        print("Head (Left): " + str(head))
        print(self.preorder)

        index = 0
        while True:
            if inorder[index] == curr:
                break
            if inorder[index] == head:
                return None
            index += 1
        
        root = TreeNode()
        root.val = self.preorder[0]
        self.preorder.pop(0)
        root.left = self.buildTreeAux_Left(inorder, root.val)
        root.right = self.buildTreeAux(inorder, head)

        return root

    def buildTreeAux(self, inorder, head):
        if not self.preorder:
            return None

        curr = self.preorder[0]
        
        print("Head (Right): " + str(head))
        print(self.preorder)

        index = 0
        while True:
            if inorder[index] == curr:
                break
            if inorder[index] == head:
                return None
            index += 1

        root = TreeNode()
        root.val = self.preorder[0]
        
        self.preorder.pop(0)
        root.left = self.buildTreeAux_Left(inorder, root.val)
        if self.preorder:
            root.right = self.buildTreeAux(inorder, head)

        return root
    
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        return self.buildTreeAux(inorder, 3001)
        

test = Solution()
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
preorder = [3,1,2,5,4]
inorder = [1,5,2,3,4]
result = test.buildTree(preorder, inorder)


def printTree(node):
    if node:
        print(node.val)
        printTree(node.left)
        printTree(node.right)
    else:
        print(None)

printTree(result)