package Array.Hard;

/*
 * 493. Reverse Pairs
 * Using concept of Merge sort we can solve this
 */

class Solution {
    public int reversePairs(int[] arr) {
        int n = arr.length;
        int res = mergeSort(arr, 0, n - 1);
        // System.out.println(Arrays.toString(arr));
        return res;
    }

    private int mergeSort(int[] arr, int left, int right) {
        int count = 0;
        if (left < right) {
            int mid = (left + right) / 2;
            count += mergeSort(arr, left, mid);
            count += mergeSort(arr, mid + 1, right);
            count += merge(arr, left, mid, right);
        }
        return count;
    }

    private int merge(int[] arr, int left, int mid, int right) {
        int n = mid - left + 1;
        int m = right - mid;
        int[] L = new int[n];
        int[] R = new int[m];

        // storing left and right half in temp arrays
        for (int i = 0; i < n; i++) {
            L[i] = arr[left + i];
        }
        for (int j = 0; j < m; j++) {
            R[j] = arr[mid + 1 + j];
        }

        // calculating reverse pairs
        int count = 0;
        int tempStart = 0;
        for (int ind=0; ind<R.length; ind++) {
            while (tempStart<L.length && (long) R[ind]*2 >= L[tempStart]) {
                tempStart++;
            }
            count += L.length-tempStart;
        }

        int i = 0, j = 0, k = left;

        while (i < L.length && j < R.length) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }

        while (i < L.length) {
            arr[k++] = L[i++];
        }

        while (j < R.length) {
            arr[k++] = R[j++];
        }

        return count;
    }
}
