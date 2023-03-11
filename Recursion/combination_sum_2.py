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
        backtrack(ind+1, arr, curr, res, n ,target, currsumm) # to get combination_sum_1 -> just make function call for ind and not for ind+1 

        currsumm -= arr[ind]
        curr.pop()

    return res

def backtrack2(i, arr, res, curr, n, target, currsum):
    
    if target == currsum:
        res.append(curr.copy())
        # print(curr)
        return
    
    if i == n:
        return
        
    # pick
    curr.append(arr[i])
    currsum += arr[i]
    backtrack2(i+1, arr, res, curr, n, target, currsum)

    # not_pick
    while True:
        if i < n-1 and arr[i] == arr[i+1]:
            i += 1
        else:
            break
    curr.pop()
    currsum -= arr[i]
    backtrack2(i+1, arr, res, curr, n, target, currsum)

    # return
    return res

arr = [10,1,2,7,6,1,5]
arr.sort()
target = 8

print(backtrack2(0, arr, [], [], len(arr), target, 0))