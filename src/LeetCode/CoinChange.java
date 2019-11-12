package LeetCode;

import java.util.Arrays;

public class CoinChange {

    public static void main(String[] args) {
        CoinChange solution = new CoinChange();
        System.out.println(solution.coinChange(new int[] {2}, 3));
    }
    int result = Integer.MAX_VALUE;
    int amount;

    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        this.amount = amount;
        backtrack(coins, new int[coins.length], 0, 0);
        return result == Integer.MAX_VALUE ? -1 : result;
    }

    public void backtrack(int[] coins, int [] usedCoins, int numCoins, int usedAmount) {
        if (usedAmount == amount && numCoins < result) result = numCoins;
        else if (usedAmount < amount && numCoins < result) {
            for (int i = coins.length-1; i >= 0; i--) {
                usedCoins[i]++;
                numCoins++;
                usedAmount += coins[i];
                backtrack(coins, usedCoins, numCoins, usedAmount);
                usedCoins[i]--;
                numCoins--;
                usedAmount -= coins[i];
            }
        }
    }
}
