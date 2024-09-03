package Misc;

/*
 * 852. Peak Index in a Mountain Array
 */

class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int n = arr.length;
        int startingIndex = 0;
        int endIndex = n-1;

        while(endIndex >= startingIndex) {
            int mid = startingIndex + ((endIndex - startingIndex) / 2);
            int possiblePrev = mid==0 ? 0 : arr[mid-1];
            int possibleNext = mid==n-1 ? 0 : arr[mid+1];
            if (arr[mid] > possiblePrev && arr[mid] > possibleNext) {
                return mid;
            }else if (arr[mid] < possiblePrev) {
                endIndex = mid - 1;
            }else {
                startingIndex = mid + 1;
            }
        }
        return startingIndex;
    }
}