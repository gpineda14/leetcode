def findRedundantConnection(edges):
    graph = collections.defaultdict(set)

    def findPath(src, target, seen):
        if src not in seen:
            seen.add(src)
            if src == target:
                return True
            return any(findPath(node, target, seen) for node in graph[src])

    for u, v in edges:
        seen = set()
        if u in graph and v in graph and findPath(u, v, seen):
            return u, v
        graph[u].add(v)
        graph[v].add(u)
