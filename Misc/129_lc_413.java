/*
 * 413. Arithmetic Slices
 */

class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int startIndex = 0;
        int endIndex = 0;
        int n = nums.length;
        Integer currDiff = null;
        int res = 0;

        while (endIndex < n && startIndex < n - 2) {
            if (currDiff == null) {
                endIndex++;
                if (endIndex < n) {
                    currDiff = nums[endIndex] - nums[startIndex];
                }
                continue;
            }

            while (endIndex < n - 1 && nums[endIndex + 1] - nums[endIndex] == currDiff) {
                endIndex++;
            }

            int subarrayLength = endIndex - startIndex + 1;
            if (subarrayLength >= 3) {
                res += (subarrayLength - 1) * (subarrayLength - 2) / 2;
            }

            startIndex = endIndex;
            currDiff = null; // Reset for the next segment
        }

        return res;
    }
}
