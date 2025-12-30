def backtrack(i, res, currsum, arr, n):
    if i == n:
        res.append(currsum)
        # print(curr)
        return

    # pick
    currsum += arr[i]
    backtrack(i + 1, res, currsum, arr, n)

    # not_pick
    currsum -= arr[i]
    backtrack(i + 1, res, currsum, arr, n)

    # return
    # res.append(0)
    return res


arr = [1, 2, 3]
print(*backtrack(0, [], 0, arr, len(arr)))
