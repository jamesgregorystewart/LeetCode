package Playground;

public class QuickSort {

    public static void main(String[] args) {
        QuickSort sort = new QuickSort();
        int[] unordered = new int[] {1,4,3,5,6,2,7};
        sort.quicksort(unordered, 0, unordered.length - 1);
        for (int n : unordered) System.out.println(n);
    }

    public void quicksort(int[] array, int left, int right) {
        int l = left, r = right;
        int pivot = array[left + (right - left) / 2];

        while (l <= r) {
            while (array[l] < pivot) l++;
            while (array[r] > pivot) r--;

            if (l <= r) {
                int temp = array[l];
                array[l] = array[r];
                array[r] = temp;
                l++;
                r--;
            }
        }
        if (left < r) quicksort(array, left, r);
        if (l < right) quicksort(array, l, right);
    }
}
