package Array.Medium;

/*
 * 2149. Rearrange Array Elements by Sign
 */

class Solution {
    public int[] rearrangeArray(int[] nums) {
        int numsLen = nums.length;
        int[] res = new int[numsLen];
        int posInd = 0;
        int negInd = 1;

        for (int num : nums) {
            if (num < 0) {
                res[negInd] = num;
                negInd += 2;
            }else {
                res[posInd] = num;
                posInd += 2;
            }
        }
        return res;
    }
}