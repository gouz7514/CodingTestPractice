# 캠핑
# 문제 링크 : https://www.acmicpc.net/problem/4796
# 문제 이해 : 1분
# 문제 해결 : 7분 30초
# 수학적으로 잘 해결한 것 같다
i = 0
while True:
    i += 1
    L, P, V = map(int, input().split())
    if L == 0:
        break
    print('Case {0}:'.format(i), (V // P) * L + min(V % P, L))