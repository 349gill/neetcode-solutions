class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (len(edges) == 0 and n == 1): return True      # Single Node

        connected_nodes = set(edges[0])         # Set of Connected Nodes
        for edge in edges[1:]:
            if (edge[0] in connected_nodes or edge[1] in connected_nodes):
                connected_nodes.add(edge[0])
                connected_nodes.add(edge[1])
        
        if (len(connected_nodes) != n):
            return False                        # Graph is disconnected

        return len(edges) == n - 1              # Check whether E = V - 1
        