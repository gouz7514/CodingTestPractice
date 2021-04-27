# A → B
# 문제 링크 : https://www.acmicpc.net/problem/16953
# 문제 이해 : 1분 30초
# 문제 해결 : 8분 20초
# queue에 넣는 방법도 있구나
##########################
# 내 풀이
# A, B = map(int, input().split())
# ans = 0

# while A < B:
#     if B % 10 == 1: # 1로 끝나면
#         B //= 10
#         ans += 1
#     elif B % 10 in [3,5,7,9]: # 3,5,7,9로 끝나면
#         ans = -1
#         break
#     else:
#         B //= 2
#         ans += 1
# if A == B:
#     print(ans+1)
# else:
#     print(-1)
#########################
# 남의 풀이
# queue에 (a, 1)을 넣는다.
# popleft를 통해 뽑은 숫자에서 가능한 연산을 한다.
# 2를 곱했을 때 b보다 크다면 queue에 넣지 않는다.
# 1을 수의 가장 오른쪽에 추가했을 때 b보다 크면 queue에 넣지 않는다.
from collections import deque

a,b = map(int, input().split())
res = -1
que = deque([(a,1)])

while que:
    i, cnt = que.popleft()
    if i == b:
        res = cnt
        break
    if i * 2 <= b:
        que.append((i*2, cnt+1))
    if int(str(i)+'1') <= b:
        que.append((int(str(i)+'1'), cnt+1))

print(que)
print(res)