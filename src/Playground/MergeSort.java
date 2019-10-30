package Playground;

public class MergeSort {

    public static void main(String[] args) {
        MergeSort sort = new MergeSort();
        int[] unordered = new int[] {1,6,2,5,3,4,7,4,2,5};
        sort.mergeSort(unordered, unordered.length);
        for (int n : unordered) System.out.println(n);
    }

    public void mergeSort(int[] array, int n) {
        if (n < 2) return;

        int mid = n / 2;
        int[] l_array = new int[mid];
        int[] r_array = new int[n - mid];

        for (int i = 0; i < mid; i++) l_array[i] = array[i];
        for (int i = mid; i < n ; i++) r_array[i - mid] = array[i];

        mergeSort(l_array, mid);
        mergeSort(r_array, n - mid);
        merge(array, l_array, r_array, mid, n - mid);
    }

    public void merge(int[] array, int[] l_array, int[] r_array, int l, int r) {
        int a_pointer = 0, l_pointer = 0, r_pointer = 0;

        while (l_pointer < l && r_pointer < r) {
            if (l_array[l_pointer] < r_array[r_pointer])
                array[a_pointer++] = l_array[l_pointer++];
            else
                array[a_pointer++] = r_array[r_pointer++];
        }
        while (l_pointer < l) array[a_pointer++] = l_array[l_pointer++];
        while (r_pointer < r) array[a_pointer++] = r_array[r_pointer++];
    }
}
