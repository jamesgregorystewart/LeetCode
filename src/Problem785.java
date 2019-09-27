import java.util.Arrays;
import java.util.Stack;

class Problem785 {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        Arrays.fill(color, -1);

        for (int start = 0; start < n; ++start) { //iterate through every member of the graph in case it isn't strongly connected
            if (color[start] == -1) { // only touch if uncolored
                Stack<Integer> stack = new Stack(); // to keep track of neighbors to evaluate
                stack.push(start);
                color[start] = 0; //

                while (!stack.empty()) {
                    Integer node = stack.pop();
                    for (int nei: graph[node]) { //check all neighbors
                        if (color[nei] == -1) { // if uncolored
                            stack.push(nei); // store the neighbor to check its neighbors
                            color[nei] = color[node] ^ 1; // set the neighbor to opposite of previous
                        } else if (color[nei] == color[node]) { //if colored make sure it is not the same color as its neighbor
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
}