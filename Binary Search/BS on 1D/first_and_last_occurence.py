def find(arr,n,target):
    
    # to find starting index
    left = 0
    right = n-1
    start = -1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            start = mid
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    # to find ending index
    left = 0
    right = n-1
    end = -1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            end = mid
            left = mid + 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return [start, end]