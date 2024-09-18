package Array.Medium;

/*
 * 54. Spiral Matrix
 */
import java.util.*;
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int n=matrix.length;
        int m=matrix[0].length;
        int startR=0;
        int startC=0;
        int endR = n-1;
        int endC = m-1;
        List<Integer> res = new ArrayList<>();

        while (startR<=endR && startC<=endC) {
            // left to right
            for (int i=startC; i<=endC; i++) {
                res.add(matrix[startR][i]);
            }
            startR++;

            // top to bottom
            for (int i=startR; i<=endR; i++) {
                res.add(matrix[i][endC]);
            }
            endC--;

            // left to right
            if (startR <= endR) {
                for (int i=endC; i>=startC; i--) {
                    res.add(matrix[endR][i]);
                }
            }
            endR--;

            // bottom to top
            if (startC <= endC) {
                for (int i=endR; i>=startR; i--) {
                    res.add(matrix[i][startC]);
                }
            }
            startC++;
        }

        return res;
    }
}