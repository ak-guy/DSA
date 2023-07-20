arr = [10, 9, 2, 5, 3, 7, 101, 18]
# arr = [1, 1, 1, 1, 1]
n = len(arr)
count = 1

dp = [1 for i in range(n)] # at any index it will store the maximum length acheived till that index
hash = [0 for j in range(n)] # at any index it will store the index of maximum length acheived previously  
for i in range(n):
    hash[i] = i
    for j in range(0,i):
        if arr[i] > arr[j] and 1+dp[j] > dp[i]:
            hash[i] = j
            dp[i] = max(dp[i],1+dp[j])
            count = max(count, dp[i])
print(*hash)
print(*dp)
print(count)

start_index = dp.index(count)
res = []
while start_index >= 0:
    if hash[start_index] == start_index:
        res.append(arr[start_index])
        break
    res.append(arr[start_index])
    start_index = hash[start_index]

print(res[::-1])