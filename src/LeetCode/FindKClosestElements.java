package LeetCode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class FindKClosestElements {

    public static void main(String[] args) {
        FindKClosestElements solution = new FindKClosestElements();
        System.out.println(solution.findClosestElements(new int[] {0,0,1,2,3,3,4,7,7,8}, 3, 5));
    }

    /*
    * Plan: binary search for the target
    *       -> then iterate outwards with two pointers adding the one that is closest to the target, prefer left
    * */

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        if (arr == null || arr.length == 0) return new LinkedList<>();
        LinkedList<Integer> result = new LinkedList<>();

        if (x <= arr[0]) for (int i = 0; i < k && i < arr.length; i++) result.add(arr[i]);
        if (result.size() > 0) return result;
        if (x >= arr[arr.length-1]) for (int i = arr.length - 1; i >= 0 && i > arr.length - (k + 1); i--) result.addFirst(arr[i]);
        if (result.size() > 0) return result;

        int left = 0;
        int right = arr.length - 1;

        while (left + 1 < right && result.size() == 0) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == x) result = addClosest(arr, x, k, mid);
            else if (arr[mid] < x && arr[mid + 1] > x) result = addClosest(arr, x, k, arr[mid+1] - x > x - arr[mid] ? mid : mid + 1);
            else if (arr[mid] > x && arr[mid - 1] < x) result = addClosest(arr, x, k, arr[mid] - x > x - arr[mid-1] ? mid-1 : mid);
            else if (x < arr[mid]) right = mid;
            else left = mid;
        }
        if (result.size() == 0) result = addClosest(arr, x, k, arr[right] - x < x - arr[left] ? right : left);
        return result;
    }

    /*
    * [0,0,1,2,3,3,4,7,7,8]
        3
        5
    * */

    public LinkedList<Integer> addClosest(int[] arr, int x, int k, int idx) {
        LinkedList<Integer> result = new LinkedList<>();
        result.add(arr[idx]);
        int left = idx - 1;
        int right = idx + 1;
        while (result.size() < k) {
            if (left < 0 && right > arr.length - 1) break;
            else if (left < 0) result.add(arr[right++]);
            else if (right > arr.length - 1) result.addFirst(arr[left--]);
            else if (x - arr[left] <= arr[right] - x) {
                result.addFirst(arr[left--]);
            }
            else result.add(arr[right++]);
        }
        return result;
    }
}
