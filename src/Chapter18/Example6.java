package Chapter18;

import java.util.*;

public class Example6 {

    public void start() {
        //create graph
        //call cloneGraph
        //print graph + cloned graph
    }

    class GraphVertex {
        int label;
        List<GraphVertex> edges;

        public GraphVertex(int label, List<GraphVertex> edges) {
            this.label = label;
            this.edges = edges;
        }
    }

    public GraphVertex cloneGraph(GraphVertex root) {
        if (root == null) return null;

        Stack<GraphVertex> stack = new Stack();
        stack.add(root);
        Map<GraphVertex, GraphVertex> map = new HashMap();

        while(!stack.isEmpty()) {
            GraphVertex node = stack.pop();
            if (!map.containsKey(node)) {
                GraphVertex clone = new GraphVertex(node.label, node.edges);
                map.put(node, clone);
                for (GraphVertex neighbor : node.edges) {
                    stack.push(neighbor);
                }
            }
        }
        return map.get(root);
    }
}
