# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
# Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
# The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

# Input: edges = [1,2,-1], node1 = 0, node2 = 2
# Output: 2
# Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
# The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.



def closestMeetingNode(edges, node1, node2):
    return





if __name__ == "__main__":
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    print(closestMeetingNode(edges, node1, node2))

    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    print(closestMeetingNode(edges, node1, node2))