/*
 * 526. Beautiful Arrangement
 */

class Solution {
    public int countArrangement(int n) {
        int[] res = new int[1]; // Use array to allow modification in helper
        int[] used = new int[n + 1]; // Tracks used numbers

        helper(1, n, used, res);
        return res[0];
    }

    private void helper(int currIndex, int n, int[] used, int[] res) {
        // Base case
        if (currIndex > n) {
            res[0]++;
            return;
        }

        for (int numberToPut = 1; numberToPut <= n; numberToPut++) {
            if (used[numberToPut] == 0 && (numberToPut % currIndex == 0 || currIndex % numberToPut == 0)) {
                used[numberToPut] = 1; // Mark number as used
                helper(currIndex + 1, n, used, res); // Recurse
                used[numberToPut] = 0; // Backtrack
            }
        }
    }
}
