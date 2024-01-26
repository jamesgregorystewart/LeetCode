# GRAPHS

[Table of Contents](#table-of-contents)

## Table of Contents

1. [Disjoint Sets](#disjoint-sets)
2. [Depth-First Search](#depth-first-search)
3. [Breadth-First Search](#breadth-first-search)
4. [Minimum-Spanning Tree](#minimum-spanning-tree)
5. [Single Source Shortest Path Algorithm](#single-source-shortest-path-algorithm)
6. [Khan's Algorithm](#khans-algorithm)

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
Eulerian Path is a trail in a finite graph that visits every edge exactly once. A Eulerian circuit is a Eulerian path that starts and ends at the same vertex. Allowing for revisiting vertices. Basic idea is a stepwise construction of the Eulerian cycle by connecting disjunctive circles. The two steps involved are:

- It starts with an arbitrary node and then follows an arbitrary unvisited edge from the graph/adjacnecy list to a neighbor. This step is repeated by marking these edges as used, or removing them from the graph (i.e. popping them from the collection).
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

## Breadth-First Search

Most advantageous case for "breadth-first search" is to efficiently find the shortest path between two vertices in a "graph" where all edges have equal and positive weight.

### Tips

You can process elements by level by processing the length of the queue at a time. I.e. all nodes 1 level from origin, all nodes 2 levels from origin, etc. This may be useful when trying to find the minimum path from a point, can be either a tree, graph or matrix. Another thing to note here is the use of the is_valid_move() function to check whether the next move is valid or not.

Problem: [Shortest Path in Binary Matrix](https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3896/)

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] != 0:
            return -1

        queue = collections.deque()
        queue.append((0,0)) # x, y, path_dist
        moves = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        seen = [[False] * len(grid[0]) for _ in range(len(grid))]
        seen[0][0] = True

        # Let's make sure we stay in bounds
        def is_valid_move(row, col) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and \
                grid[row][col] == 0

        path_length = 1
        while queue:
            band = len(queue)
            for _ in range(band):
                row, col = queue.popleft()
                if row == len(grid)-1 and col == len(grid[0]) - 1:
                    return path_length
                for move in moves:
                    n_row, n_col = [a + b for a, b in zip([row, col], move)]
                    if is_valid_move(n_row, n_col) and not seen[n_row][n_col]:
                        seen[n_row][n_col] = True
                        queue.append((n_row, n_col))
            path_length += 1
        return -1
```

#### Get Candidates/Neighbors with position validation

When doing BFS in a matrix, it is often useful to validate the next set of positions are valid. A trick to do that is to create a function which does this validation simply, and yields the candidates for simple use in a loop.

```python
def get_neighbors(row, col):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for row_diff, col_diff in directions:
        n_row, n_col = row + row_diff, col + col_diff
        if not (0 <= n_row < n and 0 <= n_col < m):
            continue
        if grid[n_row][n_col] != 1:
            continue
        yield (n_row, n_col)

minutes = -1
while queue:
    minutes += 1
    band = len(queue)
    for _ in range(band):
        row, col = queue.popleft()
        for orange in get_neighbors(row, col):
            grid[orange[0]][orange[1]] = 2
            fresh -= 1
            queue.append(orange)
```

## Minimum Spanning Tree

Two algorithms take charge here when solving undirected weighted graph problems, typically minimizing or maximizing the path, or weight of the tree or graph.

### Kruskal's Algorithm

The basic idea here is that we will create all possible edges, sort them by weight, then add them to a UnionFind DS if they are unconncected to iteratively add all the edges greedily in order of smallest weight until we have a fully connected tree or graph.

Problem: [Minimum Spanning Tree](https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3858/)

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        uf = UnionFind(size)

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                # Calculate the distance between two coordinates.
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                pq.append(edge)

        # Convert pq into a heap.
        heapq.heapify(pq)

        result = 0
        count = size - 1
        while pq and count > 0:
            edge = heapq.heappop(pq)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                result += edge.cost
                count -= 1
        return result

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

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

if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()
    print(f"points = {points}")
    print(f"Minimum Cost to Connect Points = {solution.minCostConnectPoints(points)}")
```

### Prim's Algorithm

The basic idea here is that we are going to add one vertex at a time to our MST by first creating all edges from the first point, adding them to a minheap, and then iteratively pop off the edges, checking the second point on whether it has been seen. If it hasn't we'll add the vertex in that min-cost edge to our graph, adjusting the cost and count, and then add all possible edges from that vertex to the heap.

Problem: [Minimum Spanning Tree](https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3858/)

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        visited = [False] * size
        result = 0
        count = size - 1
        # Add all edges from points[0] vertexs
        x1, y1 = points[0]
        for j in range(1, size):
            # Calculate the distance between two coordinates.
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, j, cost)
            pq.append(edge)

        # Convert pq to a heap.
        heapq.heapify(pq)

        visited[0] = True
        while pq and count > 0:
            edge = heapq.heappop(pq)
            point1 = edge.point1
            point2 = edge.point2
            cost = edge.cost
            if not visited[point2]:
                result += cost
                visited[point2] = True
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                                   abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq, Edge(point2, j, distance))
                count -= 1
        return result

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()
    print(f"points = {points}")
    print(f"Minimum Cost to Connect Points = {solution.minCostConnectPoints(points)}")
```

## Single Source Shortest Path Algorithm

BFS is great at finding shortest path in an unweighted graph. When the graph is weighted, we must turn to the single-source shortest path algorithm. TBC these will be great algorithms when solving weighted, directed shortest-path problems.

### Edge Relaxation

This is the process by which we map distances between the source and its connected vertices by "relaxing", that is identifying shorter paths through other vertices to a target. E.g. A -> D may be `4`, but A -> C is `1` and C -> D is `1`, so we can relax A -> D from `4` to `3`.

### Dijkstra's Algorithm

“Dijkstra’s algorithm” solves the “single-source shortest path” problem in a weighted directed graph with non-negative weights.

We take the starting point u as the center and gradually expand outward while updating the “shortest path” to reach other vertices.

“Dijkstra's Algorithm” uses a “greedy approach”. Each step selects the “minimum weight” from the currently reached vertices to find the “shortest path” to other vertices. It is because this algorithm is greedy that negative weights do not work. If negative weights were permissible then locally optimal choices may not lead to a globally optimal solution due to the creation of cycles. Negative weights may cause the algorithm to revisit and potentially update the distrances of previously visited vertices.

This involves setting the distances to all vertices from the target as infinity and iterating through, updating the distance to each vertex as the min. We will maintain a set of processed nodes to prevent looking back at vertices we have already processed and computed a minimum distance to for.

In other terms, we will use a heap to prioritize those available paths to take from some location to which we navigated to with the weight used in ordering the shortest path. From the node we popped off the queue/heap we will find all adjacent nodes, if not visited we will add those next paths to the queue with the weight of what it cost to get to the source node *plus* the weight to get to that next node.

Problem: [Network Delay Time](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3863/)

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times or n < 2:
            return -1

        # Build adj matrix
        graph: Dict[int, List[Tuple[int, int]]] = collections.defaultdict(list)
        for src, to, weight in times:
            graph[src].append((to, weight))
        queue = [(0, k)]  # This is a min heap to sort paths by shortest
        processed = set()
        max_cost = 0

        """
        We are going to continue popping off the node with the shortest path, taking
        what is the current delay get where we were previously and adding the weight
        to the adjacent nodes and putting those back onto the queue. Once we have
        visited all of the nodes, and the queue is empty, we will be able to return
        what we have calculate to be the max delay along the longest path in the graph.
        """

        while queue:
            weight, node = heapq.heappop(queue)
            if node in processed:
                continue
            for adj_node, adj_weight in graph[node]:
                if adj_node not in processed:
                    heapq.heappush(queue, (weight + adj_weight, adj_node))
            processed.add(node)
            max_cost = max(max_cost, weight)

        return max_cost if len(processed) == n else -1

```

### Bellman Ford Algorithm

Allows negative-weight edges, but must not have any negative weight cycles. That is a cycle with a sum of weights that is negative. This would result in a negative infinity weight when cycling that path infinite times. Thus there is no shortest path when there is a negative cycle in a graph.

#### Approaches
1) The naive approach which is to use an optimized dynamic programming design which is required when there is a limit such as finding the path between two nodes using "at most k edges".
2) The optimized approach wherein you traverse the adjacency graph mapping min distance to each node from the source regardless of number of edges used. Continue to do this until the shortest path to each node stops going down, at which point you can exit/return.

##### DP approach

Recurrence relation for DP approach is `dp[k][u] = min(dp[k][u], dp[k-1][v] + W(u,v))`. This recurrence relation explains that the shortest path to some vertex u using at most k edges is equal to the min between the currently mapped min distance to that vertex and the min distance to some other vertex v plus the distance from v to u. Easy.

#### Detecting Negative Weight Cycles
After relaxing each edge N-1 times, perform the Nth relaxation. If you continue to detect shorter edges in the graph, then there is a negative weight cycle and thus no shortest path.

#### SPFA Algorithm 

To address the limitations, we introduce an improved variation of the Bellman-Ford algorithm by using a queue. This improvement is known as “the Shortest Path Faster Algorithm” (SPFA algorithm).

Instead of choosing among any untraversed edges, as one does by using the “Bellman-Ford” algorithm, the “SPFA” Algorithm uses a “queue” to maintain the next starting vertex of the edge to be traversed. Only when the shortest distance of a vertex is relaxed and that the vertex is not in the “queue”, we add the vertex to the queue. We iterate the process until the queue is empty. At this point, we have calculated the minimum distance from the given vertex to any vertices.

Data structures used here:
- Adjacency List/Matrix
- queue
- seen set

#### Problems

DP Bellman Ford
[Cheapest Flights within K Stops](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3866/)
```python
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        costs = [float("inf")] * n

        costs[src] = 0
        for _ in range(k + 1):
            temp = costs.copy()
            for start, end, price in flights:
                # Below checks if we have yet been to where we are starting from
                if costs[start] != float("inf"):
                    temp[end] = min(temp[end], costs[start] + price)
            costs = temp
        return costs[dst] if costs[dst] != float("inf") else -1
```

## Khan's Algorithm

Khan's Algorithm is a kind of "Topological Sort". Topological Sorting provides a linear sorting based on the required ordering between vertices in directed acyclic graphs. To be specific, given vertices u and v, to reach vertex v, we must have reached vertex u first. In “topological sorting”, u has to appear before v in the ordering. The most popular algorithm for “topological sorting” is Kahn’s algorithm.

Important Concepts:
- In-Degree -> number of arrows pointing into it
- Out-Degree -> number of arrows pointing out of it

Steps:
1. Look at all nodes in graph and make note of their In-degrees. When we see a node with an In-Degree of 0 we add it to the queue.
2. pop off from queue, marking popped node as visited, and then search the graph for nodes that are pointed at by that popped node, lowering their In-Degrees by 1. For any node that hits an in-degree of 0 should be put into the queue.
3. When queue is empty and all nodes are marked as completed then we are done.

If there are no nodes with an In-Degree of 0 then there is a cycle, then there is no topological relationship and it cannot be sorted.

Data Structures:
- queue
- completed "set"; for marking nodes that have been popped from the queue (test whether this marking of nodes is really required)

Limitations:
- “Topological sorting” only works with graphs that are directed and acyclic.
- There must be at least one vertex in the “graph” with an “in-degree” of 0. If all vertices in the “graph” have a non-zero “in-degree”, then all vertices need at least one vertex as a predecessor. In this case, no vertex can serve as the starting vertex.

Complexity Analysis:
- Time Complexity O(V + E)
    - First, we will build an adjacency list. This allows us to efficiently check which courses depend on each prerequisite course. Building the adjacency list will take O(E) time, as we must iterate over all edges.
    - Next, we will repeatedly visit each course (vertex) with an in-degree of zero and decrement the in-degree =of all courses that have this course as a prerequisite (outgoing edges). In the worst-case scenario, we will visit every vertex and decrement every outgoing edge once. Thus, this part will take O(V + E) time.
    - Therefore the total time complexity is O(E) + O(V+E).
- Space Complexity O(V+E)
    - The adjacency list uses O(E) Space
    - Storing the in-degree for each vertex requires O(V) space.
    - The queue can contain at most V nodes, so the queue also requires O(V) space.
