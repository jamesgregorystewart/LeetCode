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
| | Union-find Constructor | Find | Union | Connected |
| ----- | ----- | ------ | ----- | ------ |
| | O(N) | O(α(N)) | O(α(N)) | O(α(N)) |
