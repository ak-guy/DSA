def backtrack(i, arr, curr, res, n, target, currsumm):
    if currsumm > target:
        return
    
    if currsumm == target:
        res.append(curr.copy())
        return
    
    for ind in range(i, n):
        
        if ind > i and arr[ind] == arr[ind-1]:
            continue

        if arr[ind] > target:
            break

        currsumm += arr[ind]
        curr.append(arr[ind])
        backtrack(ind, arr, curr, res, n ,target, currsumm)

        currsumm -= arr[ind]
        curr.pop()
        # backtrack(ind+1, arr, curr, res, n ,target, currsumm)


    return res

arr = [7,2,6,5]
arr.sort()
target = 16

print(backtrack(0, arr, [], [], len(arr), target, 0))