package BinarySearch.BS_On_1D;

class Solution {
    public long findFloor(long arr[], int n, long x) {
        if (x<arr[0]) return -1;

        int l = 0;
        int r = n-1;
        while (l < r) {
            int mid = l + (r-l)/2 ;
            long currVal = arr[mid];
            
            if (l==mid) {
                return arr[l+1] <= x ? l+1 : l;
            }
            
            if (currVal == x) return mid;
            else if (currVal < x) l=mid;
            else r=mid-1;
        }
        return l;
    }
}