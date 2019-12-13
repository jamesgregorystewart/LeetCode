package LeetCode;

public class FriendCircles {

    public static void main(String[] args) {
        FriendCircles solution = new FriendCircles();
        System.out.println(solution.findCircleNum(new int[][] {{0,0,0},
                                                                {0,0,0},
                                                                {0,0,0}}));
    }

    /*
        Example 1:
        Input:
        [[1,1,0],
         [1,1,0],
         [0,0,1]]
        Output: 2
        Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
        The 2nd student himself is in a friend circle. So return 2.

        Example 2:
        Input:
        [[1,1,0],
         [1,1,1],
         [0,1,1]]
        Output: 1
        Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
        so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

        Note:
        N is in range [1,200].
        M[i][i] = 1 for all students.
        If M[i][j] = 1, then M[j][i] = 1.


        Note:
        - if a row is all 0s then decrement the number of friendgroups
        - when doing the union between two people if the value is true then decrement the
            number of friendgroups
        - if during a union the value is false then do not decrement the number of friendgroups
    * */

    //TODO: I did this right per my understanding but my understanding was incorrect
    // M[i][j] == 1 means that persons i and j are friends
    //TODO: Revise below code to solve correct problem

    public int findCircleNum(int[][] M) {
        int friendgroups = M.length;
        DSU dsu = new DSU(M[0].length);

        //iterate through the friend groups
        for (int i = 0; i < M.length; i++) {
            int left = 0;
            //find the first person
            while (left < M[i].length && M[i][left] != 1) left++;
            //if no one was found
            if (left == M[i].length) {
                friendgroups--;
                continue;
            }
            //now find more people and build the group
            int right = left + 1;
            if (right == M[i].length) continue; //first person was last person
            do {
                if (M[i][right] == 1) {
                    if (dsu.union(left, right)) friendgroups--; //shrink num of groups
                }
                right++;
            } while(right < M[i].length);
        }
        return friendgroups;
    }

    private class DSU {
        int[] parent;
        int[] rank;

        DSU (int size) {
            parent = new int[size];
            for (int i = 0; i < size; i++) parent[i] = i;
            rank = new int[size];
        }

        //validate this
        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        public boolean union(int x, int y) {
            int px = find(x); int py = find(y);
            if (px == py) return false;
            else if (rank[px] > rank[py]) parent[py] = px;
            else if (rank[px] < rank[py]) parent[px] = py;
            else {
                parent[py] = px;
                rank[px]++;
            }
            return true;
        }
    }
}
