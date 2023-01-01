# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

class Solution(object):
    ### Using BFS
    def validPath(n, edges, source, destination):
        ### a way to store all the edges in 'graph'
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ### Store all the nodes to be visited in 'queue'
        seen = [False]*n
        seen[source] = True
        queue = [source] ### collections.deque([source])

        while queue:
            curr_node = queue.pop(0) ##  queue.popleft()  more optimized code
            if curr_node == destination:
                return True

            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)
        return False

if __name__=="__main__":
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    print(Solution.validPath(n, edges, source, destination))

    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    print(Solution.validPath(n, edges, source, destination))


# ### DFS: Recursive
# def validPath(n, edges, source, destination):
#     graph = [[] for _ in range(n)]
#     for a, b in edges:
#         graph[a].append(b)
#         graph[b].append(a)
        
#     seen = [False] * n
    
#     def dfs(curr_node):
#         if curr_node == destination:
#             return True
#         if not seen[curr_node]:
#             seen[curr_node] = True
#             for next_node in graph[curr_node]:
#                 if dfs(next_node):
#                     return True
#         return False
#     return dfs(source)

## DFS: Iterative
# def validPath(n, edges, source, destination):
    # # Store all edges according to nodes in 'graph'.
    # graph = [[] for _ in range(n)]
    # for a, b in edges:
    #     graph[a].append(b)
    #     graph[b].append(a)
    
    # # Start from source node, add it to stack.
    # seen = [False] * n
    # seen[source] = True
    # stack = [source]
    
    # while stack:
    #     curr_node = stack.pop()
    #     # Add all unvisited neighbors of the current node to stack 
    #     # and mark them as visited.
    #     for next_node in graph[curr_node]:
    #         if next_node == destination:
    #             return True
    #         if not seen[next_node]:
    #             seen[next_node] = True
    #             stack.append(next_node)
    
    # return seen[destination]