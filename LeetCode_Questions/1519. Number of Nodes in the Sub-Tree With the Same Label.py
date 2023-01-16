# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
# Output: [2,1,1,1,1,1,1]
# Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
# Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).

# Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
# Output: [4,2,1,1]
# Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
# The sub-tree of node 3 contains only node 3, so the answer is 1.
# The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
# The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.

# Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
# Output: [3,2,1,1,1]


def countSubTrees(n, edges, labels):
    tree = [[] for _ in range(n)]
    for src, dest in edges:
        tree[src].append(dest)
        tree[dest].append(src)
    
    arr_dict = {}
    for i in range(len(labels)):
        arr_dict.update({labels[i]:0})

    arr = [0 for _ in range(n)]
    visited = [False] * n


    def dfs_subtree(node):
        if not visited[node]:
            visited[node] = True
            arr_dict[labels[node]] += 1

            for childNode in tree[node]:
                arr_dict[labels[childNode]] += dfs_subtree(childNode)[labels[childNode]] 
            arr[node] = arr_dict[labels[node]]
        return arr_dict
    dfs_subtree(0)
    return arr




if __name__ == '__main__':
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    labels = 'abaedcd'
    print(countSubTrees(n, edges, labels))

