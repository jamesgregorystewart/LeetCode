package LeetCode;

public class SearchSortedArrayOfUnknownSize {

    public static void main(String[] args) {

    }

    public int search(ArrayReader reader, int target) {

        int left = 0;
        int right = Integer.MAX_VALUE;
        int size = 0;
        //get the size of the array

        while (left < right) {
            size = left + (right - left) / 2;
            int n = reader.get(size);
            if (n != Integer.MAX_VALUE && reader.get(size+1) == Integer.MAX_VALUE) break; //we found the end
            else if (n != Integer.MAX_VALUE) left = size + 1;
            else right = size;
        }
        if (size == 0 && reader.get(right) != Integer.MAX_VALUE) size = right;

        left = 0;
        right = size;
        while (left <= size) {
            int mid = left + (right - left) / 2;
            int n = reader.get(mid);
            if (n == target) return mid;
            else if (target < n) right = mid - 1;
            else left = mid + 1;
        }
        return -1;
    }

    private class ArrayReader {

        private int get(int size) {
            return 0;
        }
    }
}
