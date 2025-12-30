class Solution:
    def nextPermutation(self, N, arr):
        bp = -1  # this breakpoint will point to the index where arr[bp+1:N] will be sorted in dec order
        for i in range(N - 2, -1, -1):
            if arr[i + 1] > arr[i]:
                bp = i
                break

        # if there is no point breakpoint, then that means array is sorted in reverse order, so its next perm will be rev(arr)
        if bp == -1:
            return arr[::-1]

        # now to the right of index bp we need to just greater element than arr[bp] and swap it
        last = N - 1
        while last > bp:
            if arr[last] > arr[bp]:
                arr[last], arr[bp] = arr[bp], arr[last]
                break
            last -= 1

        # reverse the arr[bp+1:], we need to reverse the remaining array because it is sorted in decreasing order, so on reversing will change its sorting
        bp = bp + 1
        last = N - 1
        while bp < last:
            arr[bp], arr[last] = arr[last], arr[bp]
            bp += 1
            last -= 1

        return arr
