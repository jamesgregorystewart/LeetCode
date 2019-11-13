package LeetCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CampusBikes {

    /*
    * Approach: bucket sort
    *
    * Idea: We will iterate through all combinations of workers and bikes and store
    * their locations in a dist array at the index of their distance. We will subsequently
    * iterate through the array of distances until all workers have been assigned. We will
    * also ensure that we do not overwrite any mappings of worker to bike.
    *
    * w = number of workers
    * b = number of bikes
    * Time: O(wb)
    * Space: O(wb)
    * */

    public int[] assignBikes(int[][] workers, int[][] bikes) {
        List<int[]>[] distances = new List[2000]; // an array that can store all possible distances
        int w = workers.length; int b = bikes.length;
        int[] wA = new int[w];
        int[] bA = new int[b];
        Arrays.fill(wA, -1); // "-1" will indicate that the ith worker has not yet been assigned a bike
        Arrays.fill(bA, -1);

        //calculate all of the distances
        for (int i = 0; i < w; i++) { //workers
            for (int j = 0; j < b; j++) { //bikes
                int[] worker = workers[i];
                int[] bike = bikes[j];
                int distance = Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
                if (distances[distance] == null) distances[distance] = new ArrayList<>();
                distances[distance].add(new int[] {i, j}); //add the worker / bike assignment to that destination index
            }
        }

        //assign the workers and bikes here
        int assignments = 0;
        for (int i = 0; i < 2000 && assignments < w; i++) {
            if (distances[i] == null) continue; //no pairs with this distance exist
            for (int[] pair : distances[i]) {
                if (wA[pair[0]] == -1 && bA[pair[1]] == -1) {
                    wA[pair[0]] = pair[1];
                    bA[pair[1]] = pair[0];
                    assignments++;
                }
            }
        }

        return wA;
    }
}
