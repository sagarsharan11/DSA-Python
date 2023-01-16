# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Input: root = []
# Output: []

# Input: root = [1]
# Output: [1]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    __idx=0
    
    @classmethod
    def buildTree(self, nodes):
        print("idx---->",Solution.__idx)
        Solution.__idx += 1
        print("Node---->",nodes[Solution.__idx])
        if nodes[Solution.__idx] is None or nodes[Solution.__idx] == -1:
            return None

        newNode = TreeNode(nodes[Solution.__idx])
        newNode.left = self.buildTree(nodes)
        newNode.right = self.buildTree(nodes)
        return newNode
    
    def preorderTraversal(self, root):
        if root is None:
            return []
        return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))


if __name__ == "__main__":
    # root = [1,None,2,3]
    # bt = Solution()
    # root = bt.buildTree(root)
    # print(root.val)
    # print(bt.preorderTraversal(root))

    root = []
    bt = Solution()
    root = bt.buildTree(root)
    # print(tn.preorderTraversal(bst))

    # root = [1]
    # tn = TreeNode()
    # bst = tn.buildTree(root)
    # print(tn.preorderTraversal(bst))