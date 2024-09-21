'''
in this problem we can check whether arr[m] == arr[m+1] or arr[m] == arr[m-1], and check the length 
of (m-l) if it is even or odd and then proceed accordingly
'''
def singleNonDuplicate(arr):
    n = len(arr)
    l, r = 0, n-1
    while l <= r:
        m = (l+r) // 2

        if m == n-1: # when we reached the end of the array
            return arr[m]
        
        if arr[m] != arr[m-1] and arr[m] != arr[m+1]: # case when middle element is the single element in array
            return arr[m]
        
        if arr[m] == arr[m+1]:
            if (m-l) % 2:
                r = m-1
            else:
                l = m+2 # need to exclude the m+1 index as m and m+1 index element is same
        else:
            if not (m-l) % 2:
                r = m-2 # need to exclude the m-1 index as m and m-1 index element is same
            else:
                l = m+1
    return arr[l]