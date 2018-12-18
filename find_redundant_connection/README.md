# 684. Redundant Connection #

**In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.**

## Understanding the problem ##

Given an undirected graph, we want to remove an unnecessary edge from the graph. We define an unnecessary edge as a edge that is not needed to reach undiscovered nodes.

If we get multiple redundant edges, then we want to return the edge that appears last in the 2d array. The input given is a 2d array that has two vertices u and v where u < v. We know the number of vertices is equal to the length of the 2d array. We also know that the input can be converted to a graph and that particular can reach all the nodes.

The output we want is an edge that is represented as an array with 2 values. Some issues that I notice is that we can't do a dfs search because if we did, we mess up the ordering. For example doing a dfs search to find all necessary paths for a list like [[1, 2], [1, 3], [2, 3]] would return [1, 3] because a dfs search would search first [1, 2] and then [2, 3]. W

We want to search through the edges and find all its nodes, but also want to preserve the order. What we also can do is for every edge, we check if there is a path from u to v. If there already is a path from u to v, then we know we have found the redundant edge.

## Concrete Examples ##

Given [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
return [1, 4]

Given [[1, 3], [2, 3], [1, 2]]
return [1, 2]

Given [[1, 2], [2, 3], [1, 4], [3, 4]]
return [3, 4]

## Break it down ##

1. Create dictionary for the graph. The value will be the set of nodes it connects to.
2. Iterate through the edges
3. Create visited set to keep track of which vertices have already been seen.
4. If both vertices u and v are in the graph and there is a path from u to v, then we have found the redundant edge
5. Create a function that checks if there is a path from u to v.
6. If there is not path from u to v, then add the edge to graph.
