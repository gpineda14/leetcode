def build_graph(rooms):
    graph = collections.defaultdict(list)
    for i in range(len(rooms)):
        graph[i] = rooms[i]
    return graph

def dfs(rooms, visited, curr):
    visited[curr] = True
    neighbors = rooms[curr]
    for neighbor in neighbors:
        if not visited[neighbor]:
            dfs(rooms, visited, neighbor)

def canVisitAllRooms(rooms):
    graph = build_graph(rooms)
    visited = [False for i in range(len(rooms))]
    visited[0] = True
    vertices = graph[0]
    for vertex in vertices:
        if not visited[vertex]:
            dfs(rooms, visited, vertex)

    return all(visited)
