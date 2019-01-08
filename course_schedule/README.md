# 207. Course Schedule #

**There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?**

## Understanding the problem ##

We are asked to see if the prerequisites in our courses are valid. If we had a course a with prerequisite course b, we can say it course prerequisites are valid if b does not have a as a prerequisite. We can model this into a graph problem if we set courses as nodes and have directed edges pointing from course to prerequisite. So any arrows pointing out of a course is considered a prerequisite. This shows us that we model it as a graph, then we also check if there is a cycle in the graph. If there is a cycle in the graph, then we know the prerequisites are not valid.

We are given two arguments as input. The first argument is the number of courses which will be an integer and the second is a list of prerequisites requirements. Each requirement contains the course along with its prerequisites. We need to return a boolean that indicates whether the prerequisites are valid which means we need to see if the graph has a cycle.

## Concrete Examples ##

Given 2, [[1, 0]]
return true

Given 2, [[1, 0], [0, 1]]
return false

Given 2, []
return true

Given 3, [[2, 1], [1, 0], [0, 2]]
return false

Given 4, [[1, 0], [2, 1]]
return true

 Given 3, [[1, 2], [1, 0], [2, 0]]
 return false

## Break it down ##

1. Create a defaultdict collections variable to hold adjacency list
2. create a visited variable to keep track of which vertices have been visited
3. convert prerequisites to adjacency list
4. do a modified dfs search on the graph to check for cycles
  - iterate from 0 to n - 1
  - if not visited, use dfs helper and check visited to true
  - check visited to false after to keep looking at every path
