# 병든 나이트
# 문제 링크 : https://www.acmicpc.net/problem/1783
# 문제 이해 : 4분 30초
# 문제 해결 : 28분 47초
# 이해가 어려웠는데 범위 나눠서 굉장히 잘 풀은 것 같다.
# 아, 범위를 다 나누지 말고 min을 써서 더 쉽게 풀 수 있구나
N, M = map(int, input().split())  # 세로, 가로
answer = 0

if N >= 3:
    if M >= 6:
        answer = M - 2 # 4 + (M - 6) : 처음 6칸은 모든 이동 방법 포함해야함
    else:
        answer = min(4, M)
elif N == 2:
    answer = min(4, (M + 1) // 2)
elif N == 1:
    answer = 1

print(answer)