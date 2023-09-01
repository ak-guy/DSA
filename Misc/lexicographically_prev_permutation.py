# # very much similar to Next Permutation
class Solution:
    def prevPermutation(self, s):
        arr = [int(i) for i in s]
        N = len(arr)
        bp = -1 # this breakpoint will point to the index where arr[bp+1:N] will be sorted in inc order
        for i in range(N-2,-1,-1):
            if arr[i+1] < arr[i]:
                bp = i
                break
        
        # if there is no point breakpoint, then that means array is sorted in inc order, so its prev perm will be None
        if bp == -1:
            return "None"
        
        last = N-1
        while last > bp:
            if arr[last] < arr[bp]:
                arr[last], arr[bp] = arr[bp], arr[last]
                break
            last -= 1
        
        # reverse the arr[bp+1:], we need to reverse the remaining array because it is sorted in decreasing order, so on reversing will change its sorting
        bp = bp+1
        last = N-1
        while bp < last:
            arr[bp], arr[last] = arr[last], arr[bp]
            bp += 1
            last -= 1
        
        return "".join(str(i) for i in arr)