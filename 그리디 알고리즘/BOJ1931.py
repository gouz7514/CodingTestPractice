# 회의실 배정
# 문제 링크 : https://www.acmicpc.net/problem/1931
n = int(input())
meeting = []
answer = 0
x = 0

for i in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda start: start[0])
meeting.sort(key=lambda end: end[1])

for i in range(n):
    if (meeting[i][0] >= x):
        answer += 1
        x = meeting[i][1]

print(answer)