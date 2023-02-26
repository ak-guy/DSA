def solve(arr1, arr2, n, m, k):
    if n > m: # always do binary search on smaller length array
        return solve(arr2, arr1, m, n, k)
        
    INT_MIN = 0-1e10
    INT_MAX = 1e10
    low = max(0, k-m) # this low will be greater than 0 in case if we have to take something from the first array. Ex- n=3, m=6, k=7 in this case we need atleast one value from first array
    high = min(n, k) # no need to search after k if k is smaller that n
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        # if cut1 == 0 then it means we dont need any element and so on
        l1 = INT_MIN if cut1 == 0 else arr1[cut1-1]
        l2 = INT_MIN if cut2 == 0 else arr2[cut2-1]
        r1 = INT_MAX if cut1 == n else arr1[cut1]
        r2 = INT_MAX if cut2 == m else arr2[cut2]
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)    
        elif l1 > r2:
            high = cut1-1
        else:
            low = cut1+1

arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
n = len(arr1)
m = len(arr2)
k = 5

print(solve(arr1, arr2, n, m, k))