package BinarySearch.BS_On_1D;


class Solution {
    public long findCeil(long arr[], int n, long x) {
        if (x>arr[n-1]) {
            return -1;
        }
        
        int l = 0;
        int r = n-1;
        while (l < r) {
            int mid = l + (r-l)/2;
            long currVal = arr[mid];
            
            if (l==mid) {
                return arr[l] >= x ? l : l+1;
            }
            
            if (currVal == x) return mid;
            else if (currVal > x) r=mid;
            else l=mid+1;
        }
        
        return l;
    }
}