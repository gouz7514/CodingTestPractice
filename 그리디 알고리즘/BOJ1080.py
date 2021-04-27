# 행렬
# 문제 링크 : https://www.acmicpc.net/problem/1080
# 문제 이해 : 45초
# 문제 해결 : 27분 40초
# 그리디로 잘 풀은 것 같다. 현재 상황에서 최적의 해결방안 구함
# 배열이 작아도 3*3 부분행렬이 나올 수가 있구나
N, M = map(int, input().split())
A = []
B = []
answer = 0

for i in range(N):
    A.append(list(input()))

for i in range(N):
    B.append(list(input()))

for i in range(N-2): # 0
    for j in range(M-2): # 0, 1
        if A[i][j] != B[i][j]: # 어차피 다르다면 무조건 뒤집어야됨
            for k in range(i, i+3):
                for l in range(j, j+3):
                    A[k][l] = '1' if A[k][l] == '0' else '0'
            answer += 1

if A == B:
    print(answer)
else:
    print(-1)