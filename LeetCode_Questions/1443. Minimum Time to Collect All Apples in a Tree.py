# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows. 

# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
# Output: 0

### TOPIC: GRAPHS (Every Tree is a Graph, but not every Graph is a Tree) | DFS | Traversal


## BFS | replace edges parameter with graph
def minTime(n, graph, hasApple):
    graph = [[] for _ in range(n)]
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    
    print(graph)

    apple_found = 0

    visited = [False] * n

    queue = []  ### this is used to append index
    idx = 0

    if hasApple[idx] == True:
        apple_found += 1
    queue.append(idx)
    visited[idx] = True

    while idx < len(queue):
        curr = queue[idx]
        idx += 1

        for node in graph[curr]:
            if not visited[node]:
                if hasApple[node] == True:
                    apple_found += 1
                visited[node] = True
                queue.append(node)
    
    return apple_found




        



if __name__ == "__main__":
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,True,True,False]
    print(minTime(n, edges, hasApple))
