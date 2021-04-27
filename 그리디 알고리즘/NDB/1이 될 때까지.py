N, K = map(int, input().split())
cnt = 0

# 내 풀이 : N이 1이 아닐때 순차적으로 연산 수행
while N != 1:
    if N % K == 0:
        N //= K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)

# 나동빈 풀이
result = 0

while True:
    target = (N // K) * K # 나누어 떨어지는 제일 큰 수
    result += (N - target) # 1을 빼는 횟수 계산
    N = target

    if N < K:
        break
    # K로 나누기
    result += 1
    N //= K
# 마지막으로 남은 수에 대해 1씩 빼기
result += (N - 1)
print(result)