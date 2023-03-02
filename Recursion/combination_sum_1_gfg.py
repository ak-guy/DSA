def backtrack(i, arr, curr, res, n, target, currsumm):
    if currsumm > target or i == n:
        return
    
    if currsumm == target:
        res.append(curr.copy())
        return
    
    while True:
        if i < n-1 and arr[i] == arr[i+1]:
            i += 1
        else:
            break

    # pick
    currsumm += arr[i]
    curr.append(arr[i])
    backtrack(i, arr, curr, res, n, target, currsumm)

    # not pick
    currsumm -= arr[i]
    curr.pop()
    backtrack(i+1, arr, curr, res, n, target, currsumm)

    return res

arr = [2,3,4,5]
arr.sort()
target = 8

print(backtrack(0, arr, [], [], len(arr), target, 0))