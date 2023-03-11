def backtrack(i, res, curr, arr, n):
    if i == n:
        res.append(curr.copy())
        # print(curr)
        return
        
    # pick
    curr.append(arr[i])
    backtrack(i+1, res, curr, arr, n)

    # not_pick
    while True:
        if i < n-1 and arr[i] == arr[i+1]:
            i += 1
        else:
            break
    curr.pop()
    backtrack(i+1, res, curr, arr, n)

    # return
    return res

arr = [1,1,1,2,2]
arr.sort()
print(backtrack(0, [], [], arr, len(arr)))