class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        found_nodes = set()

        for i in range(n):
            if i not in found_nodes:
                found_nodes = self.dfs(i, edges, found_nodes)
                components += 1
            
        return components

    def dfs(self, start, edges, found_nodes):
        stack = []
        visited = set()
        stack.append(start)
        while len(stack) != 0:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for edge in edges:
                    if (edge[0] == current and edge[1] not in visited):
                        stack.append(edge[1])
                    elif (edge[1] == current and edge[0] not in visited):
                        stack.append(edge[0])
        
        return visited.union(found_nodes)

                        



        
