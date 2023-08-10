def solve(arr,target):

    N = len(arr)
    M = len(arr[0])

    # start = arr[0][-1]

    i, j = 0, M-1
    while True:
        if target == arr[i][j]:
            return 1
        elif target > arr[i][j]:
            i += 1
        else:
            j -=1
        
        if i == N or j == -1:
            return 0

arr = [[10, 20, 30, 40], 
       [15, 25, 35, 45], 
       [27, 29, 37, 48], 
       [32, 33, 39, 50]]
target = 50
print(solve(arr, target))
