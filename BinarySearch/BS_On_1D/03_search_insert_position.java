package BinarySearch.BS_On_1D;

/*
 * 35. Search Insert Position
 */

class Solution {
    public int findCeil(int arr[], int n, int x) {
        if (x>arr[n-1]) {
            return n;
        }
        
        int l = 0;
        int r = n-1;
        while (l < r) {
            int mid = l + (r-l)/2;
            int currVal = arr[mid];
            
            if (l==mid) {
                return arr[l] >= x ? l : l+1;
            }
            
            if (currVal == x) return mid;
            else if (currVal > x) r=mid;
            else l=mid+1;
        }
        
        return l;
    }

    public int searchInsert(int[] nums, int target) {
        return findCeil(nums, nums.length, target);
    }
}