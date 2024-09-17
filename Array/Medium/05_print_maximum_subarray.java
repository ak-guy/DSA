package Array.Medium;

class Solution {
    public int maxSubArray(int[] nums) {
        /*
        Here we are printing the subarray with the largest sum too
        */
        int res = nums[0];
        int curr = 0;
        int currWindowSum = 0;
        int start = 0;
        int ansStart = -1;
        int ansEnd = -1;

        while (curr < nums.length) {
            if (currWindowSum == 0) start = curr;
            currWindowSum += nums[curr];

            if (currWindowSum >= res) {
                ansEnd = curr;
                ansStart = start;
                res = currWindowSum;
            }
            if (currWindowSum < 0) {
                currWindowSum = 0;
            }
            curr++;
        }
        for (int j=ansStart; j<=ansEnd; j++) {
            System.out.print(nums[j] + ", ");
        }
        return res;
    }
}