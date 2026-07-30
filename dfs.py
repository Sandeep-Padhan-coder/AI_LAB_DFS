def dfs(graph, start_node):
    visited=[]
    stack=[start_node]

    while stack:
        current_node=stack.pop()

        if current_node not in visited :
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            for neighbour in graph.get(current_node, []):
                if neighbour not in visited:
                    stack.append(neighbour)

    return visited
# Create Graph
graph = {}

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v = input("Enter edge (u v): ").split()

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []
    
    graph[u].append(v)
    graph[v].append(u)

print("\nGraph =", graph)

start = input("Enter starting node: ")

if start not in graph:
    print("Starting node does not exist in the graph.")
else:
    result = dfs(graph, start)
    print("\nBFS Traversal:", result)
