# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Input: p = [1,2,1], q = [1,1,2]
# Output: false


### Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution  :
    __idx = -1
    
    @classmethod
    def buildTree(self,nodes):
        if Solution.__idx >= len(nodes) - 1:
            return None
        # print("idx---->",Solution.__idx)
        Solution.__idx += 1
        # print("Node---->",nodes[Solution.__idx])
        if nodes[Solution.__idx] is None:
            return None

        newNode = TreeNode(nodes[Solution.__idx])
        newNode.left = self.buildTree(nodes)
        newNode.right = self.buildTree(nodes)

        return newNode

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (p.val==q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    p = [1,2,3]
    q = [1,2,3]
    s1 = Solution()
    s2 = Solution()
    tr1 = s1.buildTree(p)
    tr2 = s2.buildTree(q)
    print(tr1.val)
    print(tr2.val)
    # print(sol.isSameTree(p,q))