package LeetCode;

public class TrappingRainWater {

    public static void main(String[] args) {
        TrappingRainWater solution = new TrappingRainWater();
        System.out.println(solution.trap(new int[] {0,1,0,2,1,0,1,3,2,1,2,1}));
    }

    public int trap(int[] height) {
        if (height.length < 3) return 0;

        int left = 0;
        int right = 1;
        int blocks = 0;
        int ans = 0;

        /*
        * need to keep storing volumes as algo traverses right, then add them to final when height[right] >= height[left] ->
        * then move left to right and right+1
        * */

        //left to right
        while (right < height.length) {
            if (right - left == 1 && height[left] == 0) { //minor optimization
                left++;
                right++;
            }
            else if (height[right] < height[left]) {
                blocks += height[right++];
            }
            else if (height[right] >= height[left]) {
                //add highest volume in between both to
                int h = Math.min(height[left], height[right]);
                ans += h * (right - left - 1) - blocks;
                left = right;
                right++;
                blocks = 0;
            }
        }

        int tRight = height.length-1;
        int tLeft = height.length-2;
        blocks = 0;

        //right to left
        while (tLeft >= left) {
            if (height[tLeft] < height[tRight])
                blocks += height[tLeft--];
            else if (height[tLeft] >= height[tRight]) {
                int h = Math.min(height[tLeft], height[tRight]);
                ans += h * (tRight - tLeft - 1) - blocks;
                tRight = tLeft;
                tLeft--;
                blocks = 0;
            }
        }

        return ans;
    }
}
