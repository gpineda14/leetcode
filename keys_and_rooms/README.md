# 841. Keys and Rooms #

**There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.**

## First Thoughts/Questions ##

So we want to see if we can enter every room. Every room contains a set of keys that open other rooms.

Here are some things we know to be true:

- There are len(rooms) many rooms
- Room 0 is the only room open
- Each room may have some keys to access the next room

This resembles a graph problem because we can use each room i as a vertex and the list of keys rooms[i] in each room as an edge from vertex i to vertex rooms[i][j].

With this information, we can modify the rooms list into a adjacency list, mapping the index i of rooms to the sublist rooms[i].

## First Approach ##

Because we want to see if we can enter every room, we need to keep track of all the rooms visited. We will create a list called visited of size len(rooms) and set every element to false. Because Room 0 has no key and is our starting point, we will set visited[0] to True.

What we want to do then is a depth-first search with Room 0 as the starting point. We will then run a depth-first search on all of Room's 0 keys. After doing a dfs on all of keys in Room 0, we will check if any of rooms in rooms have not been visited. If at least 1 has not been visited, we return false. 
