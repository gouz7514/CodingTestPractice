# 알바생 강호
# 문제 링크 : https://www.acmicpc.net/problem/1758
# 문제 이해 : 1분 20초
# 문제 해결 : 3분
# 오 이건 엄청 쉽게 풀음 ㅋㅋ
tip = []
answer = 0

for _ in range(int(input())):
    tip.append(int(input()))

tip.sort(reverse=True)
for i in range(len(tip)):
    money = tip[i] - i
    if money > 0:
        answer += money
print(answer)