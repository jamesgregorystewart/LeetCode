# GRAPHS

## Disjoint Sets

Disjoint Sets are often used to determine if two nodes are connected.
Disjoint Sets are implemented as arrays where the index is the number, and the value
is its parent. When the index and value are the same, then you have found the root.

### Disjoint Set Implementation

find() - returns the root of a node
union() - combines two nodes into the same disjoint set; choosing a new root if required.

Disjoint set can be designed as "Quick Find" or "Quick Union" with the one optimized to O(1)
and the other up to O(N).

#### QuickFind() Implementation

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

#### QuickUnion Implementation

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

Note: QuickUnion is the generally more efficient implementation

### Union By Rank

Union by Rank is an optimization for Quick Union Disjoint Sets to protect against the worst-case instance of a linear tree, causing O(n) find().

To be more efficient we can use "rank" to determine the new root of a union, instead of using x, or y, each time.
This will allow us to limit the height of the tree and can avoid worst case instances of a tree being a line.

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Path Compression Optimization

Path Compression is an optimization for QuickUnion Disjoint Sets to speed up the find() operation.

To find the root node, we need to traverse the parent nodes sequentially until we reach the root node. If we search the root node of the same element again, we repeat the same operations. Can we optimize this? Yes!

Using recursion we can efficiently, and simply set the parent node of all traversed nodes to the root for quick find() operations in the future.

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Optimized Disjoint Set with Union by Rank and Path Compression

```python
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

Putting our two optimization to QuickUnion Disjoint Sets together we can achieve a Time Complexity Table of
| Union-find Constructor | Find | Union | Connected |
| ----- | ------ | ----- | ------ |
| O(N) | O(α(N)) | O(α(N)) | O(α(N)) |

O(α(N)) refers to the Inverse Ackermann function. In practice assume it's a constant, or O(1).

## Depth-First Search

Now we will consider, given a graph, how will we find all of its vertices and how can we find all paths between two vertices.

In graph theory, DFS is mainly used to:

1. Traverse all vertices in a "graph"
2. Traverse all paths between any two vertices in a "graph"

Data structures used:

- _Stack_ to track untraversed paths, or vertices; Note that if you are traversing all paths between two points, you will be storing the full path in the stack.
- _Set_ to track where you have been, what has been visited.

### Traversing all vertices in graph

- Stack will track all vertices connected by edge to current vertex
- Set will track vertices that have been visited

When pulling off the stack, check if the vertex has been visited, if so, continue popping off stack until a vertex you have not visited appears

### Traversing all paths between two points

- Stack will track all paths available from current vertex
- Set will track visited vertices as part of a current path; set of visited will remove vertices as you backtrack to attempt other paths; unmark a vertex as visited if there are no valid paths from that vertex

### Implementation

1. First step is typically to create an adjacency map to allow for quick lookups and prevent references to input array. This will take the form of a `graph = collections.defaultdict(list)` so that you may quickly append edges

```python
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
```

2. A "seen" _Set_ will track where you have been: `seen = [False] * n`

### Recursive Example

```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)
```

### Iterative Example

```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Store all edges according to nodes in 'graph'.
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Start from source node, add it to stack.
        seen = [False] * n
        seen[source] = True
        stack = [source]

        while stack:
            curr_node = stack.pop()
            # Add all unvisited neighbors of the current node to stack
            # and mark them as visited.
            for next_node in graph[curr_node]:
                if next_node == destination:
                    return True
                if not seen[next_node]:
                    seen[next_node] = True
                    stack.append(next_node)

        return seen[destination]
```

### Specialized Algorithms

#### Hierholzer's Algorithm to find Eulerian Path

Problem: [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/editorial/)
Eulerian Path is a trail in a finite graph that visitts every edge exactly once. Allowing for revisiting vertices. Basic idea is a stepwise construction of the Eulerian cycle byu connecting disjuunctive circles. The two steps involved are:

- It starts with a random node and then follows an arbitrary unvisited edge to a neighbor. This step is repeated until one returns to the starting node. This yields the first circle in the graph.
- If this circle covers all nodes it is an Eulerian cycle and the algorithm is finished. Otherwise, one chooses another node among the cycles' nodes with unvisited edges and constructs another circle, called subtour.

The general path followed can be managed with sorting graph contents, or by choosing a starting point.

To summarize, the main idea to find the Eulerian path consists of two steps:

Step 1). Starting from any vertex, we keep following the unused edges until we get stuck at certain vertex where we have no more unvisited outgoing edges.

Step 2). We then backtrack to the nearest neighbor vertex in the current path that has unused edges and we repeat the process until all the edges have been used.

Sample simple backtracking DFS with precise starting point and lexicographically sorted graph.

```python
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)
```

#### Using Memoization, DFS, Backtracking all together

Problem: [All Paths from Source Lead to Destination](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/description/)

```python
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1 create graph
        self.graph = collections.defaultdict(list)
        for start, end in edges:
            self.graph[start].append(end)

        """
        Cache results on whether we can reach end or not from a point
        to short-circuit where possible. Also allows us to share a single
        reference to the graph and not do any deep copies
        """
        @lru_cache(None)
        def dfs(start) -> bool:
            destinations = self.graph[start]
            if destinations and start == destination:
                return False
            if not destinations:
                return start == destination
            leads_to_dest = True
            while destinations:
                next_end = destinations.pop()
                leads_to_dest &= dfs(next_end)
            return leads_to_dest

        return dfs(source)
```
