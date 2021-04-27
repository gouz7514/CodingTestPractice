arr = list(map(int, input()))
answer = arr[0]

for i in range(1, len(arr)):
    if arr[i] <= 1 or answer <= 1:
        answer += arr[i]
    else:
        answer *= arr[i]

print(answer)