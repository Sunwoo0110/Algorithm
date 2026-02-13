num = int(input())
DP = [1] * num
arr = [0] * num

arr = list(map(int, input().split()))
    
for i in range(1, num):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))