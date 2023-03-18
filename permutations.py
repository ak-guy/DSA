def backtrack(i,arr,res,n):
    if i == n:
        res.append(arr.copy())
        return
    
    for ind in range(i, n):
        arr[ind], arr[i] = arr[i], arr[ind]
        backtrack(i+1, arr, res, n)
        arr[ind], arr[i] = arr[i], arr[ind]

    return res

arr = [1,2,3]
print(backtrack(0, arr, [], len(arr)))