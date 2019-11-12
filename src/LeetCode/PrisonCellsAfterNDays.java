package LeetCode;

public class PrisonCellsAfterNDays {

    public int[] prisonAfterNDays(int[] cells, int N) {
        int L = cells.length;
        int[] result = new int[L];

        for (int i = 0; i < L; i++) {
            result[i] = cells[i];
        }

        //O(LN) -> change cell values for each run
        for (int i = 0; i < N; i++) {
            //change the cells
            for (int j = 1; j < L-1; j++) {
                if (cells[j-1] == cells[j+1]) result[j] = 1;
                else result[j] = 0;

                //set prev vals for next iteration
                cells[j-1] = result[j-1];
            }
            //set front and back to 0 after first iteration
            if (i == 0) {
                cells[0] = 0; cells[L-1] = 0;
                result[0] = 0; result[L-1] = 0;
            }
            cells[L-2] = result[L-2];
        }
        return result;
    }
}
