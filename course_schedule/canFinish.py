def canFinish(numCourses, prerequisites):
    adjList = collections.defaultdict(list)
    visited = [False] * numCourses
    recStack = [False] * numCourses

    for pre in prerequisites:
        adjList[pre[0]].append(pre[1])

    for node in range(numCourses):
        if not visited[node]:
            if isCycle(node, visited, recStack, adjList):
                return False

    return True

def isCycle(curr, visited, recStack, adjList):
    visited[curr] = True
    recStack[curr] = True

    for node in adjList[curr]:
        if not visited[node]:
            if isCycle(node, visited, recStack, adjList):
                return True
            elif recStack[node]:
                return True

    recStack[curr] = False
    return False
