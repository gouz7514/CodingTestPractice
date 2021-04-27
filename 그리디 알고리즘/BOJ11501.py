# 주식
# 문제 링크 : https://www.acmicpc.net/problem/11501
# 문제 이해 : 1분 30초
# 문제 해결 : 30분 초과
# 계속 감소하는 경우만 아니면 사고팔고 하는게 이득이다.
# 뒤에 더 비싼 가격이 하나라도 있으면 사야 함
# 없으면 다 팔아야 함
# 그냥 뒤에서부터 순회하면 훨씬 쉬운데 왜 이걸 생각 못했냐..
# 인덱스, 조건 등으로 막히면 방향 바꿔보자
for _ in range(int(input())):
    N = int(input())
    price = list(map(int, input().split()))
    value = 0
    max_v = 0
    for i in range(N-1, -1, -1):
        if (price[i] > max_v):
            max_v = price[i]
        else:
            value += max_v - price[i]
    print(value)