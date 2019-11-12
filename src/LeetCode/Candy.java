package LeetCode;

public class Candy {

    public static void main(String[] args) {
        Candy solution = new Candy();
        System.out.println(solution.candy(new int[] {1,6,10,8,7,3,2}));
    }

    /*
    * Thoughts:
    *   - find a low point and work outwards from there
    *   - when scanning left, stop when you reach the previous right boundary
    *   - when scanning right, stop when you reach a value equal to or lower than the current value
    *      -> you will then go right to find the next low point
    *
    *      TODO: there is an issue where candies are handed to the best student but then it's right child (lower rating)
    *           TODO cont: gets the same or more candies and the better rated student requires more candies
    *
    *      Best solution will be to calculate the candies instead of incrementing them by finding the left and right lows
    *      around a peak and using the distances on left and right to calculate candies handed out instead of simulation
    * */

    private int[] ratings;
    private int candyPieces = 0;

    public int candy(int[] ratings) {
        if (ratings.length == 1) return 1;

        this.ratings = ratings;
        int leftBound = 0;
        int low;

        //O(L) runs for every low that exists, worst case N
        while(leftBound < ratings.length) {
            low = findLow(leftBound);
            leftBound = assignCandy(leftBound, low);
        }

        return candyPieces;
    }

    /*
     * Returns: index of the low point
     *
     * O(N)
     * */
    public int findLow(int start) {
        int curr = start;
        while (curr < ratings.length) {
            if (curr < ratings.length-1 && ratings[curr] <= ratings[curr+1]) return curr;
            curr++;
        }

        return ratings.length-1;
    }

    /*
    * Assigns candy to kids and returns the new leftbound location
    * */
    public int assignCandy(int leftBound, int low) {
        int right = low + 1;
        int left = low - 1;
        int candyHandout = 2;

        //add for low
        candyPieces += 1;

        //go left
        while (left >= 0 && left >= leftBound) {
            candyPieces += candyHandout++;
            left--;
        }

        candyHandout = 2;
        //go right
        while (right < ratings.length && ratings[right] > ratings[right-1]) {
            candyPieces += candyHandout++;
            right++;
        }

        return right;
    }
}
