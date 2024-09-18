package Array.Medium;

/* 48. Rotate Image
Algorithm :

    To rotate image ClockWise, take transpose of matrix then reverse every row.
    To rotate image AntiClockWise, take transpose of matrix then reverse every col.

 */

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        // taking transpose of the matrix
        for (int r=0; r<n; r++) {
            for (int c=r; c<m; c++) {
                int temp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = temp;
            }
        } 

        // reverse every row
        for (int r=0; r<n; r++) {
            int start=0;
            int end=m-1;
            while (start < end) {
                int temp = matrix[r][start];
                matrix[r][start] = matrix[r][end];
                matrix[r][end] = temp;
                start++;
                end--;
            }
        }
    }
}