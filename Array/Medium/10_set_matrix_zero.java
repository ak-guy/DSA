package Array.Medium;

/*
 * 73. Set Matrix Zeroes
 */

class Solution {
    public void setZeroes(int[][] matrix) {
        /*
        for this problem we could have used set to determine which row or col to make zero
        but that would take extra memory, instead we will modify the matrix's first row and 
        col to tell whether we have to make whole row or col zero
         */
        boolean setCol0Flag = false;
        int n = matrix.length;
        int m = matrix[0].length;

        // 
        for (int r=0; r<n; r++) {
            if (matrix[r][0] == 0) setCol0Flag=true;
            for (int c=1; c<m; c++) {
                if (matrix[r][c]==0){
                    matrix[0][c] = 0;
                    matrix[r][0] = 0;
                }
            }
        }
        
        // 
        for (int r=n-1; r>-1; r--) {
            for (int c=m-1; c>0; c--) {
                if (matrix[r][0]==0 || matrix[0][c]==0) matrix[r][c]=0;
            }
            if (setCol0Flag) matrix[r][0] = 0;
        }
    }
}