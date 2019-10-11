package LeetCode;

public class MaxDistClosestPerson {

    public static void main(String[] args) {
        MaxDistClosestPerson solution = new MaxDistClosestPerson();
        System.out.println(solution.maxDistToClosest(new int[] {1,1,0,0,0,1,0}));
    }

    public int maxDistToClosest(int[] seats) {
        if (seats.length == 0) return 0;

        int front = 0;
        int back = seats.length-1;
        int max = 0;

        int curDist = 0;
        //check front
        while(front < seats.length && seats[front++] == 0) curDist++;
        max = Math.max(curDist, max);

        curDist = 0;
        //check back
        while (back >= 0 && seats[back--] == 0) curDist++;
        max = Math.max(curDist, max);

        boolean open = true;
        curDist = 0;
        //check middle
        for (int i = front; i <= back; i++) {
            if (seats[i] == 0) {
                if (open) curDist++;
                else {
                    curDist = 1;
                    open = true;
                }
            } else {
                max = curDist % 2 == 0 ? Math.max(curDist/2, max) : Math.max(curDist/2+1, max);
                curDist = 0;
                open = false;
            }
        }
        max = curDist % 2 == 0 ? Math.max(curDist/2, max) : Math.max(curDist/2+1, max);
        return max;
    }
}
