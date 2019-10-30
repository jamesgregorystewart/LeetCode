package LeetCode;

import java.util.*;

public class EvaluateDivision {

    public static void main(String[] args) {
        EvaluateDivision solution = new EvaluateDivision();
//        System.out.println(solution.calcEquation());
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> map = new HashMap<>();
        for (int i = 0; i < values.length; i++) {
            map.putIfAbsent(equations.get(i).get(0), new HashMap<>());
            map.putIfAbsent(equations.get(i).get(1), new HashMap<>());
            map.get(equations.get(i).get(0)).put(equations.get(i).get(1), values[i]);
            map.get(equations.get(i).get(1)).put(equations.get(i).get(0), 1/values[i]);
        }
        double[] results = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            results[i] = dfs(queries.get(i).get(0), queries.get(i).get(1), 1, map, new HashSet<>());
        }
        return results;
    }

    public double dfs (String s, String t, double r, Map<String, Map<String, Double>> map, HashSet<String> seen) {
        if (!map.containsKey(s) || !seen.add(s)) return -1;
        if (s.equals(t)) return r;
        for (String next : map.get(s).keySet()) {
            double nextVal = map.get(s).get(next);
            double result = dfs(next, t, r*nextVal, map, seen);
            if (result != -1) return result;
        }
        return -1;
    }
}
