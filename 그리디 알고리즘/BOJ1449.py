# 수리공 항승
# 문제 링크 : https://www.acmicpc.net/problem/1449
# 문제 이해 : 3분 40초
# 문제 해결 :
# ??? 왜 이해가 안 됨??
# 아 ㅅㅂ ㅋㅋ leak가 정렬되있는 상태가 아니구나 ㅋㅋ
## 내 풀이
# N, L = map(int, input().split())
# leak = list(map(int, input().split()))
# answer = 0
# start = leak[0] - 0.5
# finish = leak[0] + (L - 0.5)
#
# for i in range(N):
#     if leak[i] > finish:
#         answer += 1
#         start = leak[i] - 0.5
#         finish = leak[i] + (L - 0.5)
# answer += 1
# print(answer)

## 남의 풀이
n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()
start = leak[0]
end = leak[0] + l
cnt = 1
for i in range(n):
    if start <= leak[i] < end:
        continue
    else:
        start = leak[i]
        end = leak[i] + l
        cnt += 1
print(cnt)