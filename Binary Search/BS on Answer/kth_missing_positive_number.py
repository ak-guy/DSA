'''
suppose, arr = [2,3,4,7,11]
how_it_should)be = [1,2,3,4,5] if no number was missing
missing_num = [1,1,1,3,6] these are number of missing numbers till the index 'i'

or, missing_num = arr[i] - (i + 1) this will also tell us how many number are missing till this index i

Now if this missing_num is smaller then k, then that will mean answer lies left to mid

At the end of loop, when we exit l and r will be pointing to two different indices, where r = l-1
so calculating the kth missing number,

kth_missing_num = arr[r] + (k - (missing_num[r]))
=> kth_missing_num = arr[r] + (k - (arr[r] - r - 1)) 
=> kth_missing_num = k + r + 1 
'''

class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r) // 2
            number_of_missing_integer = arr[mid] - (mid + 1)

            if number_of_missing_integer < k:
                l = mid + 1
            else:
                r = mid - 1
        
        return r+1+k